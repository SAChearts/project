import sqlite3
import hashlib


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


def load_employee(emp_id: int) -> tuple | None:
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


# if __name__ == "__main__":
#     login("lsmith", "lsmith1234")
