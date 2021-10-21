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


# if __name__ == "__main__":
#     login("lsmith", "lsmith1234")
