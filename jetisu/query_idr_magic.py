from IPython.display import display, Markdown, Latex
from jetisu.idr_query import idr_query
import hashlib


def jetisu_query(line, cell):
    display(Markdown(idr_query(cell, 'markdown table')))


def jetisu_testcase(line, cell):
    print("""def test_idr_""" + hashlib.sha1(cell.strip().encode()).hexdigest()[:10] + """():
    res = idr_query(\"\"\"""" + cell + """\"\"\", 'data')
    assert sorted_res(res) == sorted_res(""" + str(idr_query(cell, 'data')) + """)""")


def jetisu_show(line, cell):
    display(Markdown("```\n\n" + idr_query('select * from ' + cell.strip(), 'model') + "\n```"))


def jetisu_show_prepared(line, cell):
    display(Markdown("```\n\n" + idr_query(cell, 'constrained model') + "\n```"))


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
