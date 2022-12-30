# !/usr/bin/env python
# coding: utf-8

# Basic imports and setup

import json
import os
import re
import subprocess
import sys
import tempfile

from sqlglot import exp, parse_one
from sqlglot.executor import execute


def idr_read_model(canonical_table_name):
    with open('jetisu/' + canonical_table_name + '.mzn', 'r') as file:
        return file.read()


def idr_query(sql_query, return_data):
    assert return_data in ['data', 'markdown table', 'model', 'constrained model']

    # handles a conjuction of simple constraint clauses only TODO Generalise this code.
    table_name = ''
    where_clause = ''
    column_name = ''
    found_where = False
    found_constraints = False
    found_eq = False
    found_not = False
    too_complex = False
    eq_constraints = {}

    for node_tuple in parse_one(sql_query).walk(bfs=False):
        if isinstance(node_tuple[0], exp.Identifier):
            # for current purposes the Identifiers may be ignored.
            continue
        if isinstance(node_tuple[0], exp.Group) or isinstance(node_tuple[0], exp.Having) or isinstance(node_tuple[0],
                                                                                                       exp.Order):
            found_where = False
            found_constraints = False
            continue
        if isinstance(node_tuple[0], exp.Table):
            table_name = str(node_tuple[0])
            continue
        if isinstance(node_tuple[0], exp.Where):
            where_clause = str(node_tuple[0])
            found_where = True
            continue
        if found_where:
            if isinstance(node_tuple[0], exp.And):
                continue
            elif isinstance(node_tuple[0], exp.EQ) or isinstance(node_tuple[0], exp.Not) or isinstance(node_tuple[0],
                                                                                                       exp.Column):
                found_where = False
                found_constraints = True
            else:
                too_complex = True
                continue
        if found_constraints and not found_eq and not found_not:
            if isinstance(node_tuple[0], exp.EQ):
                found_eq = True
                continue
            if isinstance(node_tuple[0], exp.Not):
                found_not = True
                continue
            if isinstance(node_tuple[0], exp.Column):
                eq_constraints[str(node_tuple[0]).lower()] = True
                continue
            too_complex = True
            continue
        if found_constraints and found_eq and column_name == '':
            if isinstance(node_tuple[0], exp.Column):
                column_name = str(node_tuple[0]).lower()
                continue
            too_complex = True
            continue
        if found_constraints and found_eq and column_name != '':
            if isinstance(node_tuple[0], exp.Literal):
                # print(node_tuple[0].is_string, str(node_tuple[0]))

                eq_constraints[column_name] = str(node_tuple[0]) if node_tuple[0].is_string else float(
                    str(node_tuple[0]))
                found_eq = False
                column_name = ''
                continue
            too_complex = True
            continue
        if found_constraints and found_not:
            if isinstance(node_tuple[0], exp.Column):
                eq_constraints[str(node_tuple[0]).lower()] = False
                found_not = False
                continue
            too_complex = True
            continue

    canonical_table_name = table_name.lower()
    model = idr_read_model(canonical_table_name)
    if return_data == 'model':
        return model
    # Merge in the constraints in the query to get the model to be fed to MiniZinc

    parameters = re.search(r"predicate +" + canonical_table_name + r" *\(([^)]+?)\)", model, re.S)[1].lower()
    typed_parameters_list = [[y.lower().replace('var','').strip() for y in x.split(":")] for x in parameters.split(",")]
    variables = parameters.replace(",", ";") + ";"
    primary_constraint = 'constraint ' + canonical_table_name + '(' + ', '.join(
        [x.split(":")[1] for x in parameters.split(",")]) + ');'

    where_clause_data = '; '.join([(x + "= true" if len(x.split("=")) == 1 else x) for x in
                                   where_clause.lower().replace("where", "").split("and")]) if where_clause else ''
    constrained_model = model + "\n" + variables + "\n" + primary_constraint + "\n" + (where_clause_data + ";" if where_clause_data else '')
    model_fn = tempfile.NamedTemporaryFile().name
    mf = open(model_fn + ".mzn", 'w')
    mf.write(constrained_model)
    mf.close()

    schema_cols = {}
    for c in typed_parameters_list:
        schema_cols[c[1]] = c[0]
    schema = {canonical_table_name: schema_cols}

    if return_data == 'constrained model':
        return constrained_model

    # Run MiniZinc model and save result, starting with the opitmathsat solver
    path_to_minizinc = "C:/Program Files/MiniZinc/minizinc" if sys.platform.startswith('win32') else "/usr/bin/minizinc"
    result = subprocess.run(
        [path_to_minizinc, "--solver", "optimathsat", model_fn + ".mzn"],
        stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    data_output = []
    data = False
    column = []
    for line in output.splitlines():
        if not data:
            if line == "% allsat model":
                data = True
        if data:
            if line == "% allsat model":
                column = []
            elif line == "----------":

                data_output.append('{' + ', '.join(column) + '}')
            elif line == "==========":
                pass
            else:
                x = line.replace(";", "").split("=")
                column.append('"' + x[0].strip() + '": ' + x[1].strip())
    solver_data = json.loads('[' + ', '.join(data_output) + ']')

    # and if there is no result, then try with optimathsat
    if not solver_data:
        result = subprocess.run(
            [path_to_minizinc, model_fn + ".mzn"],
            stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        data_output = []
        data = False
        column = []
        for line in output.splitlines():
            if line == "----------":
                data_output.append('{' + ', '.join(column) + '}')
                column = []
            elif line == "==========":
                pass
            else:
                x = line.replace(";", "").split("=")
                column.append('"' + x[0].strip() + '": ' + x[1].strip())
        solver_data = json.loads('[' + ', '.join(data_output) + ']')

    os.remove(model_fn + ".mzn")

    if not solver_data:
        table_input = {canonical_table_name: []}
    else:
        # Put output into a list of dict as data ready to run
        table_input = {table_name.lower(): [x | eq_constraints for x in solver_data]}  # | eq_constraints

    # Run the query
    res = execute(
        sql_query,
        schema=schema,
        tables=table_input
    )

    if return_data == 'data':
        return res.columns, res.rows
    elif return_data == 'markdown table':
        return '|' + '|'.join(res.columns) + '|' + "\n" + '|' + '|'.join(
            ["----" for x in res.columns]) + '|' + "\n" + "\n".join(
            ['|' + '|'.join([str(val) for val in r]) + '|' for r in res.rows])
    else:
        return 'Programming error - this should never occur'

