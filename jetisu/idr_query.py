# !/usr/bin/env python
# coding: utf-8

# Basic imports and setup

import json
import os
import re
import subprocess
import sys
import tempfile
import math

from sqlglot import exp, parse_one
from sqlglot.executor import execute
from sqlglot.optimizer.lower_identities import lower_identities


def idr_read_model(canonical_table_name):
    with open('jetisu/' + canonical_table_name + '.mzn', 'r') as file:
        return file.read()

def idr_test_res_sort(res):
    return (res[0], sorted(res[1], key=lambda element: "".join([str(x) for x in element])))

def mzn_input_quote(k, v, typed_parameters_dict):
    if typed_parameters_dict[k] == 'bool':
        return str(v).lower()
    elif typed_parameters_dict[k] == 'float':
        return str(v)
    elif typed_parameters_dict[k] == 'int':
        return str(int(v))
    else:
        return str(v)  # enum's assumed to be varchar/string

def mzn_output_quote(k, v, typed_parameters_dict):
    if 'enum' in typed_parameters_dict[k]:
        return '"'+v+'"'
    else:
        return v

def sqlglot_table2md(res):
    return '|' + '|'.join(res.columns) + '|' + "\n" + '|' + '|'.join(
            ["----" for x in res.columns]) + '|' + "\n" + "\n".join(
            ['|' + '|'.join([str(val) for val in r]) + '|' for r in res.rows])

def idr_query(sql_query, return_data):
    assert return_data in ['raw', 'data', 'markdown table', 'model', 'constrained model']

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

    # see https://github.com/tobymao/sqlglot/blob/638ed265f195219d7226f4fbae128f1805ae8988/sqlglot/optimizer/lower_identities.py
    # Assuming the schema is all lower case, this essentially makes identifiers case-insensitive.
    # Implication for MiniZinc is that all parameters MUST be lowercase.
    for node_tuple in lower_identities(parse_one(sql_query)).walk(bfs=False):
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
                eq_constraints[str(node_tuple[0])] = True
                continue
            too_complex = True
            continue
        if found_constraints and found_eq and column_name == '':
            if isinstance(node_tuple[0], exp.Column):
                column_name = str(node_tuple[0])
                continue
            too_complex = True
            continue
        if found_constraints and found_eq and column_name != '':
            if isinstance(node_tuple[0], exp.Literal):
                # print(node_tuple[0].is_string, str(node_tuple[0]))

                eq_constraints[column_name] = str(node_tuple[0]).replace("'", "") if node_tuple[0].is_string else float(
                    str(node_tuple[0]))
                found_eq = False
                column_name = ''
                continue
            too_complex = True
            continue
        if found_constraints and found_not:
            if isinstance(node_tuple[0], exp.Column):
                eq_constraints[str(node_tuple[0])] = False
                found_not = False
                continue
            too_complex = True
            continue
    canonical_table_name = table_name
    model = idr_read_model(canonical_table_name)
    if return_data == 'model':
        return model
    # Merge in the constraints in the query to get the model to be fed to MiniZinc

    # Minizinc "predicate and predicate name and var and var names must be lower-case
    parameters = re.search(r"predicate +" + canonical_table_name + r" *\(([^)]+?)\)", model, re.S)[1]
    typed_parameters_list = [[y.replace('var', '').strip() for y in x.split(":")] for x in
                             parameters.split(",")]
    variables = parameters.replace(",", ";") + ";"
    primary_constraint = 'constraint ' + canonical_table_name + '(' + ', '.join(
        [x.split(":")[1] for x in parameters.split(",")]) + ');'
    where_clause_data = '; '.join(
        [k + " = " + mzn_input_quote(k, v, dict([(k, v) for v, k in typed_parameters_list])) for k, v in
         eq_constraints.items()])
    output_statement = 'output ["' + "\\n".join([k+" = \\("+k+")" for v, k in typed_parameters_list])+'"];'
    constrained_model = model + "\n" + variables + "\n" + primary_constraint + "\n" + (
        where_clause_data + ";" if where_clause_data else '') + "\n"+ output_statement
    model_fn = tempfile.NamedTemporaryFile().name
    mf = open(model_fn + ".mzn", 'w')
    mf.write(constrained_model)
    mf.close()

    if return_data == 'constrained model':
        return constrained_model

    schema_cols = {}
    for c in typed_parameters_list:
        schema_cols[c[1]] = c[0] if c[0] in {'bool', 'float', 'int'} else 'varchar'
    schema = {canonical_table_name: schema_cols}



    # Run MiniZinc model and save result, starting with the opitmathsat solver
    path_to_minizinc = "C:/Program Files/MiniZinc/minizinc" if sys.platform.startswith('win32') else "/usr/bin/minizinc"
    result = subprocess.run(
        [path_to_minizinc, "--solver", "optimathsat", model_fn + ".mzn"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
            elif "UNSATISFIABLE" in line:
                pass
            elif line == "----------":
                data_output.append('{' + ', '.join(column) + '}')
            elif line == "==========":
                pass
            else:
                x = line.replace(";", "").split("=")
                column.append('"' + x[0].strip() + '": ' + (mzn_output_quote(x[0].strip(), x[1].strip(), dict([(k, v) for v, k in typed_parameters_list])) if x[1].strip() != '-0.0' else '0.0'))
    # print('data_output', data_output)
    solver_data = json.loads('[' + ', '.join(data_output) + ']')

    # and if there is no result, then try with optimathsat
    if not solver_data:
        result = subprocess.run(
            [path_to_minizinc, model_fn + ".mzn"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
            elif "UNSATISFIABLE" in line:
                pass
            else:
                x = line.replace(";", "").split("=")
                column.append('"' + x[0].strip() + '": ' + mzn_output_quote(x[0].strip(), x[1].strip(), dict([(k, v) for v, k in typed_parameters_list])))

        solver_data = json.loads('[' + ', '.join(data_output) + ']')

    os.remove(model_fn + ".mzn")

    if not solver_data:
        table_input = {canonical_table_name: []}
    else:
        # Put output into a list of dict as data ready to run
        table_input = {table_name: [x | eq_constraints for x in solver_data]}  # | eq_constraints

    # Run the query
    res = execute(
        sql_query,
        schema=schema,
        tables=table_input
    )
    if return_data == 'raw':
        return res
    elif return_data == 'data':
        return res.columns, res.rows
    elif return_data == 'markdown table':
        return sqlglot_table2md(res)
    else:
        return 'Programming error - this should never occur'

def jetisu_goal_directed(goal_list, table_name):
    search_prompt = f"Finding {', '.join(goal_list)}, please answer the following questions ...\n"
    tables = {table_name: idr_query(f"select * from {table_name};", 'raw')}
    where_condition = ''
    residual_columns_list = []
    print(f"{search_prompt}\n")
    while not residual_columns_list:
        goal_list, tables, where_condition, residual_columns_list = jetisu_ask_next_question(goal_list, tables, where_condition)
    return tables, where_condition, residual_columns_list

def jetisu_ask_next_question(goal_list, tables, where_condition, residual_columns=''):
    table_name = list(tables.keys())[0]
    schema = tables[table_name].columns
    search_over_list = set(schema) - set(goal_list)
    cross_product_ratio = {}  # 1 = cross product, higher is better
    randomness_proxy = {}  # 1 = apparently random, higher is better
    effectiveness_ratio = {}

    res_goal = execute(f"select count(*) from (select distinct {', '.join(goal_list)} from {table_name})",
                       tables=tables)
    res_search_over = execute(f"select count(*) from (select distinct {', '.join(search_over_list)} from {table_name})",
                       tables=tables)
    if res_goal.rows[0][0] == 1 or res_search_over.rows[0][0] == 1:
        # found solution
        # tables contains residual cases which to which the relation is indifferent
        return goal_list, tables, where_condition, search_over_list

    for q in search_over_list:
        other_columns = set(schema) - set((q,))
        # do the count of distinct for q and for other cols take the division and save it.jetisu_ask_next_question
        res_all = execute(f"select count(*) from {table_name}", tables=tables)
        res_q_and_goal = execute(
            f"select count(*) from (select distinct {', '.join(goal_list + [q])} from {table_name})", tables=tables)
        res_q = execute(f"select count(*) from (select distinct {q} from {table_name})", tables=tables)
        res_other = execute(f"select count(*) from (select distinct {', '.join(other_columns)} from {table_name})",
                            tables=tables)
        # for cross product this will be 1, for primary key this will be N the cardinality of the table.
        cross_product_ratio[q] = (res_q.rows[0][0] * res_goal.rows[0][0]) / res_q_and_goal.rows[0][
            0]  # / (1+res_all.rows[0][0]-res_q_and_goal.rows[0][0])

        # calculate sum of squares
        res_sum_of_squares = execute(
            f"select sum(sos) ssos from (select {q}, count(*)*count(*) sos from {table_name} group by {q})",
            tables=tables)
        randomness_proxy[q] = math.sqrt(res_sum_of_squares.rows[0][0]) / math.sqrt(
            res_all.rows[0][0] * pow(res_all.rows[0][0] / res_q.rows[0][0], 2))

        effectiveness_ratio[q] = cross_product_ratio[q] * randomness_proxy[q] * res_q.rows[0][0]
    sortedq = sorted(effectiveness_ratio.items(), key=lambda x: x[1], reverse=True)
    chosen_q = sortedq[0][0]
    chosen_other_columns = set(schema) - set((chosen_q,))
    qlist = execute(f"select distinct {chosen_q} from {table_name}", tables=tables).rows
    enumerated_qlist = enumerate(qlist, start=1)
    prompt = '\n'.join([f"{x}) {y[0]}" for (x, y) in enumerated_qlist])
    response_valid = False
    while not response_valid:
        response = input(f"{chosen_q}?\n{prompt}")
        if response == '':
            return "Search Cancelled ..."
        try:
            response_int = int(response)
        except ValueError:
            continue
        if response_int >= 1 and response_int <= len(qlist):
            response_valid = True
            chosen_where_condition = where_condition + (" and " if where_condition else '')
            this_where_condition = f"{chosen_q}" if str(qlist[response_int - 1][0]) == "True" else (
                    f"not {chosen_q}" if str(
                        qlist[response_int - 1][0]) == "False" else (f"{chosen_q}={qlist[response_int - 1][0]}" if (
                        isinstance(qlist[response_int - 1][0], int) or isinstance(qlist[response_int - 1][0],
                                                                                  float)) else f"{chosen_q}='{qlist[response_int - 1][0]}'"))
            chosen_where_condition += this_where_condition

    retdata = execute(
        f"select distinct {', '.join(chosen_other_columns)} from {table_name} where {this_where_condition}",
        tables=tables)

    chosen_tables = {table_name: retdata}
    return goal_list, chosen_tables, chosen_where_condition, False
