from IPython.display import display, Markdown, Latex
from jetisu.idr_query import idr_query, jetisu_goal_directed, sqlglot_table2md
import hashlib
import json
from sqlglot.executor import execute

def jetisu_query(line, cell):
    display(Markdown(idr_query(cell, 'markdown table')))


def jetisu_testcase(line, cell):
    print("""def test_idr_""" + hashlib.sha1(cell.strip().encode()).hexdigest()[:10] + """():
    res = idr_query(\"\"\"""" + cell + """\"\"\", 'data')
    assert idr_test_res_sort(res) == idr_test_res_sort(""" + str(idr_query(cell, 'data')) + """)""")


def jetisu_show(line, cell):
    display(Markdown("```\n\n" + idr_query('select * from ' + cell.strip(), 'model') + "\n```"))


def jetisu_show_prepared(line, cell):
    display(Markdown("```\n\n" + idr_query(cell, 'constrained model') + "\n```"))

def jetisu_seek_goal(line, cell):
    # {
    #     "table_name": "covid_vaccinations_and_work",
    #     "goal_list": [
    #         "covid_vaccination_work_recommended_doses",
    #         "covid_vaccination_work_mandatory"
    #     ]
    # }
    request = json.loads(cell)
    goal_list = request["goal_list"]
    table_name = request["table_name"]
    tables, where_condition, residual_columns_list = jetisu_goal_directed(goal_list, table_name)
    if list(residual_columns_list)[0] != "Quit":
        answer = "## Answer\n"+sqlglot_table2md(execute(f"select distinct {', '.join(goal_list)} from {table_name}", tables=tables))
        answer += f"\n### Because\n{where_condition}\n"
        answer += "\n### Along the way, the following additional values were determined:\n"
        for col in residual_columns_list:
            res = execute(f"select distinct {col} from {table_name}", tables=tables)
            if len(res.rows) == 1:
                answer += sqlglot_table2md(res)+"\n\n"
        answer += "\n### And the following values were under-determined:\n"
        for col in residual_columns_list:
            res = execute(f"select distinct {col} from {table_name}", tables=tables)
            if len(res.rows) > 1:
                answer += sqlglot_table2md(res)+"\n\n"
        display(Markdown(answer))
    else:
        print("Q&A cancelled.")
def load_ipython_extension(ipython):
    """This function is called when the extension is
    loaded. It accepts an IPython InteractiveShell
    instance. We can register the magic with the
    `register_magic_function` method of the shell
    instance."""
    ipython.register_magic_function(jetisu_query, 'cell')
    ipython.register_magic_function(jetisu_show, 'cell')
    ipython.register_magic_function(jetisu_testcase, 'cell')
    ipython.register_magic_function(jetisu_show_prepared, 'cell')
    ipython.register_magic_function(jetisu_seek_goal, 'cell')
