import sqlite3
import hashlib
import click
from flask import current_app, g
from flask.cli import with_appcontext


def db_connect():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'],
                               detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
        return g.db
    # return sqlite3.connect('database/sample.db') #single connection to the database


def db_close(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = db_connect()
    with current_app.open_resource('database\sampledb.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(db_close)
    app.cli.add_command(init_db_command)


def employee_query(empID):
    conn = db_connect()
    emp = conn.execute(
        """SELECT 
            e.empID,
            e.username, 
            e.pass,
            e.fname, 
            e.lname, 
            e.phone,
            e.email, 
            e.title, 
            e.startdate, 
            co_name,
            e.managerID
        FROM employees e 
        JOIN company
        WHERE e.empID = ?""",
        (empID,)
    ).fetchone()
    conn.close()

    return emp


'''
def db_connect():
      return sqlite3.connect('database/sample.db')

def login(usrname, pword):
    conn = db_connect()
    cur = conn.cursor()

    # Setup query statement
    statement = "SELECT * FROM employees WHERE username=? AND pass=?"
    usrname = usrname.strip().lower()
    pword = pword.rstrip().encode()
    pword = hashlib.md5(pword).hexdigest()  # hashed pword
    vals = (usrname, pword)

    # execute query
    cur.execute(statement, vals)
    usr = cur.fetchone()
    conn.close()

    # TODO Return user data.
    if usr:
        return True
    return False
def load_emp_data(emp_id, statement, single_row=False):
    conn = db_connect()
    cur = conn.cursor()

    # execute query
    cur.execute(statement, (emp_id,))

    if single_row:
        data = cur.fetchone()
    else:
        data = cur.fetchall()

    cur.close()
    conn.close()

    return data


def load_employee(emp_id: int) -> tuple:
    statement = "SELECT fname, lname FROM employees WHERE empID=?"
    return load_emp_data(emp_id, statement, True)


def load_employees(manager_id: int) -> list:
    statement = "SELECT empID, fname, lname FROM employees WHERE managerID = ?"
    return load_emp_data(manager_id, statement)


def load_comments(emp_id) -> list:
    statement = "SELECT comments, magnitude FROM comments WHERE empID=?"
    return load_emp_data(emp_id, statement)


def load_incedents(emp_id) -> list:
    statement = "SELECT incedent_date, incedent_desc, magnitude FROM incedents WHERE empID=?"
    return load_emp_data(emp_id, statement)


def load_punctuality(emp_id) -> list:
    statement = "SELECT incedent_date, incedent_type, magnitude FROM punctuality WHERE empID=?"
    return load_emp_data(emp_id, statement)


def load_projects(emp_id) -> list:
    statement = "SELECT project_name, magnitude FROM completed_projects WHERE empID=?"
    return load_emp_data(emp_id, statement)
'''
# if __name__ == "__main__":
#     login("lsmith", "lsmith1234")
