import functools

# import hashlib # i was going to use from werkzeug.security
# import check_password_hash, generate_password_hash but we dont have a register
# implementation and idk if generat_password_hash and hashlib are the same thing

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

# change to project.db if its not working on your end
from .db import db_close, db_connect

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if session.get('user_id'):
        return redirect(url_for('Einterface.eview'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = db_connect()
        user = db.execute(
            """SELECT 
                e.empID, 
                e.fname, 
                e.lname, 
                e.email, 
                e.title, 
                e.startdate, 
                m.lname||' '||m.fname as manager
            FROM employees e 
            JOIN employees m ON m.empID = e.managerID
            WHERE e.username = ?""",
            (username,)
        ).fetchone()
        db_close()

        error = None
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['pass'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['empID']
            session['first_name'] = user['fname']
            session['last_name'] = user['lname']
            session['email'] = user['email']
            session['title'] = user['title']
            session['manager'] = user['manager']
            session['hire_date'] = user['startdate']

            return redirect(url_for('Einterface.eview'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db_connect().execute(
            'SELECT * FROM employees WHERE empID = ?', (user_id,)
        ).fetchone()

        db_close()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('Einterface.home'))

        return view(**kwargs)

    return wrapped_view
