from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import flask

from .db import db_close, db_connect, employee_query
from hashlib import md5


#from werkzeug.exceptions import abort

#from flaskr.auth import login_required
#from flaskr.db import get_db

bp = Blueprint('Einterface', __name__)


@bp.route('/')
def home():
    # Under construction
    return render_template('Einterface/home.html')


@bp.route('/eview')
def eview():
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))

    conn = db_connect()
    total = conn.execute(
        """SELECT 
            SUM(cp.magnitude) as project_sum, 
            SUM(cm.magnitude) as comment_sum, 
            SUM(i.magnitude) as incedent_sum, 
            SUM(p.magnitude) as punctuality_sum
        FROM employees e
            LEFT JOIN completed_projects cp ON e.empID = cp.empID
            LEFT JOIN comments cm ON e.empID = cm.empID
            LEFT JOIN incedents i ON e.empID = i.empID
            LEFT JOIN punctuality p ON e.empID = p.empID
        WHERE e.empID = ?""",
        (session['user_id'],)
    ).fetchone()
    g.total = total

    performance = {}
    projects = conn.execute(
        """SELECT empID, proj_name, magnitude
        FROM completed_projects
        WHERE empID = ?
        """,
        (session.get('user_id'),)
    ).fetchall()
    performance['projects'] = projects

    comments = conn.execute(
        """SELECT empID, comments, magnitude
        FROM comments
        WHERE empID = ?
        """,
        (session.get('user_id'),)
    ).fetchall()
    performance['comments'] = comments

    punctuality = conn.execute(
        """SELECT empID, incedent_date, incedent_type, magnitude
        FROM punctuality
        WHERE empID = ?
        """,
        (session.get('user_id'),)
    ).fetchall()
    performance['punctuality'] = punctuality

    incedents = conn.execute(
        """SELECT empID, incedent_date, incedent_desc, magnitude
        FROM incedents
        WHERE empID = ?
        """,
        (session.get('user_id'),)
    ).fetchall()
    performance['incedents'] = incedents
    g.performance = performance

    top = {}
    top['projects'] = conn.execute(
        """SELECT c.empID, SUM(magnitude) as mag_sum, fname, lname
        FROM completed_projects c
        JOIN employees e ON e.empID = c.empID
        GROUP BY c.empID
        ORDER BY mag_sum DESC""",
    ).fetchmany(5)

    top['comments'] = conn.execute(
        """SELECT c.empID, SUM(magnitude) as mag_sum, fname, lname
        FROM comments c
        JOIN employees e ON e.empID = c.empID
        GROUP BY c.empID
        ORDER BY mag_sum DESC""",
    ).fetchmany(5)
    g.top = top

    conn.close()
    return render_template('Einterface/elanding.html')


@bp.route('/aview', methods=('GET', 'POST'))
def aview():
    conn = db_connect()
    employees = conn.execute(
        """SELECT 
            empID,
            (fname || ' ' || lname) as name,
            username
        FROM employees 
        WHERE managerID = ?""",
        (session['user_id'],)
    ).fetchall()
    g.employees = employees

    goals = conn.execute(
        """SELECT 
            completed_projects,
            punctuality,       
            comments,          
            incedents         
        FROM goals"""
    ).fetchone()
    g.goals = goals

    progress = conn.execute(
        """SELECT 
            avg(cp.magnitude) as projects_mag,
            avg(cm.magnitude) as comments_mag,
            avg(i.magnitude) as incedents_mag,
            avg(p.magnitude) as punctuality_mag
        FROM completed_projects cp
            LEFT JOIN comments cm
            LEFT JOIN incedents i 
            LEFT JOIN punctuality p
        """
    ).fetchone()
    g.progress = progress

    conn.close()

    return render_template('Einterface/alanding.html')


@bp.route('/admin')
def employee_view():
    qryID = int(request.args.get('empID'))

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
        (qryID,)
    ).fetchone()
    g.emp = emp

    total = conn.execute(
        """SELECT 
            SUM(cp.magnitude) as project_sum, 
            SUM(cm.magnitude) as comment_sum, 
            SUM(i.magnitude) as incedent_sum, 
            SUM(p.magnitude) as punctuality_sum
        FROM employees e
            LEFT JOIN completed_projects cp ON e.empID = cp.empID
            LEFT JOIN comments cm ON e.empID = cm.empID
            LEFT JOIN incedents i ON e.empID = i.empID
            LEFT JOIN punctuality p ON e.empID = p.empID
        WHERE e.empID = ?""",
        (qryID,)
    ).fetchone()
    g.total = total

    performance = {}
    projects = conn.execute(
        """SELECT empID, proj_name, magnitude
        FROM completed_projects
        WHERE empID = ?
        """,
        (qryID,)
    ).fetchall()
    performance['projects'] = projects

    comments = conn.execute(
        """SELECT empID, comments, magnitude
        FROM comments
        WHERE empID = ?
        """,
        (qryID,)
    ).fetchall()
    performance['comments'] = comments

    punctuality = conn.execute(
        """SELECT empID, incedent_date, incedent_type, magnitude
        FROM punctuality
        WHERE empID = ?
        """,
        (qryID,)
    ).fetchall()
    performance['punctuality'] = punctuality

    incedents = conn.execute(
        """SELECT empID, incedent_date, incedent_desc, magnitude
        FROM incedents
        WHERE empID = ?
        """,
        (qryID,)
    ).fetchall()
    performance['incedents'] = incedents
    g.performance = performance

    top = {}
    top['projects'] = conn.execute(
        """SELECT c.empID, SUM(magnitude) as mag_sum, fname, lname
        FROM completed_projects c
        JOIN employees e ON e.empID = c.empID
        GROUP BY c.empID
        ORDER BY mag_sum DESC""",
    ).fetchmany(5)

    top['comments'] = conn.execute(
        """SELECT c.empID, SUM(magnitude) as mag_sum, fname, lname
        FROM comments c
        JOIN employees e ON e.empID = c.empID
        GROUP BY c.empID
        ORDER BY mag_sum DESC""",
    ).fetchmany(5)
    g.top = top

    return render_template('Einterface/empview.html')


@bp.route('/delete/employee')
def del_employee():
    if session.get('managerID'):
        return redirect(url_for('Einterface.eview'))

    emp = int(request.args.get('empID'))

    conn = db_connect()
    conn.execute(
        """DELETE FROM employees 
        WHERE empID = ?""",
        (emp,)
    )
    conn.commit()
    conn.close()

    flash(f"Account deleted for employee ID: {emp}", "del")
    return redirect(url_for('Einterface.aview', tab="EL"))


@bp.route('/setgoals', methods=['POST'])
def setgoals():
    if session.get('managerID'):
        return redirect(url_for('Einterface.eview'))

    conn = db_connect()
    conn.execute(
        """UPDATE goals
        SET completed_projects = ?,
            punctuality = ?,
            comments = ?,
            incedents = ?      
        WHERE goal = ?""",
        (request.form['completed_projects'],
         request.form['punctuality'],
         request.form['comments'],
         request.form['incedents'],
         0)
    )
    conn.commit()
    conn.close()

    flash("Goals updated", "goals")
    return redirect(url_for('Einterface.aview', tab='SG'))


@bp.route('/add_employee', methods=['POST'])
def add_employee():
    if session.get('managerID'):
        return redirect(url_for('Einterface.eview'))

    conn = db_connect()
    conn.execute(
        """INSERT INTO employees (fname, lname, title, username, 
            pass, phone, email, dob, startdate, managerID) 
        VALUES 
            (?,?,?,?,?,?,?,?,?,?)""",
        (request.form['fname'],
         request.form['lname'],
         request.form['title'],
         request.form['username'],
         md5(f"{request.form['username']}1234".encode()).hexdigest(),
         request.form['phone'],
         f"{request.form['username']}@work.com",
         request.form['dob'],
         request.form['hire_date'],
         session['user_id'])
    )
    conn.commit()
    conn.close()

    flash(f'Account created for {request.form["username"]}', "add")
    return redirect(url_for('Einterface.aview', tab='EC'))


@bp.route('/edit_employee', methods=['POST'])
def edit_employee():
    if not session.get('is_manager'):
        return redirect(url_for('Einterface.eview'))

    pass_col = "empID=?,"
    pass_val = request.form['empID']

    passwd = request.form['pass'].strip()
    if passwd:
        pass_col = "pass=?, "
        pass_val = md5(passwd.encode()).hexdigest()

    conn = db_connect()
    conn.execute(
        f"""UPDATE employees
        SET 
            fname = ?,
            lname = ?,
            username = ?,
            {pass_col}
            email = ?,
            phone = ?,
            title = ?
        WHERE empID = ?""",
        (request.form['fname'],
         request.form['lname'],
         request.form['username'],
         pass_val,
         request.form['email'],
         request.form['phone'],
         request.form['title'],
         request.form['empID'])
    )
    conn.commit()
    conn.close()

    flash("Update Successful")
    return redirect(url_for('Einterface.employee_view', empID=request.form['empID'], tab='EI'))


@bp.route('/add_project', methods=['POST'])
def add_project():
    if session.get('managerID'):
        return redirect(url_for('Einterface.eview'))

    conn = db_connect()
    conn.execute(
        """INSERT INTO completed_projects (empID, proj_name, magnitude)
        VALUES
            (?, ?, ?)""",
        (request.form['empID'],
         request.form['proj_name'],
         request.form['magnitude'])
    )
    conn.commit()
    conn.close()

    return redirect(url_for('Einterface.employee_view', empID=request.form['empID'], tab='EP', tab2='proj'))


@bp.route('/del_project', methods=['POST'])
def del_project():
    if session.get('managerID'):
        return redirect(url_for('Einterface.eview'))

    conn = db_connect()
    conn.execute(
        """DELETE FROM completed_projects
        WHERE empID=? AND proj_name=?""",
        (request.form['empID'],
         request.form['proj_name'])
    )
    conn.commit()
    conn.close()

    return redirect(url_for('Einterface.employee_view', empID=request.form['empID'], tab='EP', tab2='proj'))


@bp.route('/add_incedent', methods=['POST'])
def add_incedent():
    if session.get('managerID'):
        return redirect(url_for('Einterface.eview'))

    conn = db_connect()
    conn.execute(
        """INSERT INTO incedents (empID, incedent_date, incedent_desc, magnitude)
        VALUES
            (?,?,?,?)""",
        (request.form['empID'],
         request.form['incedent_date'],
         request.form['incedent_desc'],
         request.form['magnitude'])
    )
    conn.commit()
    conn.close()

    return redirect(url_for('Einterface.employee_view', empID=request.form['empID'], tab='EP', tab2='inc'))


@bp.route('/del_incedent', methods=['POST'])
def del_incedent():
    if session.get('managerID'):
        return redirect(url_for('Einterface.eview'))

    conn = db_connect()
    conn.execute(
        """DELETE FROM incedents
        WHERE empID=? AND incedent_desc=?""",
        (request.form['empID'],
         request.form['incedent_desc'])
    )
    conn.commit()
    conn.close()

    return redirect(url_for('Einterface.employee_view', empID=request.form['empID'], tab='EP', tab2='inc'))


@bp.route('/add_punctuality', methods=['POST'])
def add_punctuality():
    if session.get('managerID'):
        return redirect(url_for('Einterface.eview'))

    conn = db_connect()
    conn.execute(
        """INSERT INTO punctuality (empID, incedent_date, incedent_type, magnitude)
        VALUES
            (?,?,?,?)""",
        (request.form['empID'],
         request.form['incedent_date'],
         request.form['incedent_type'],
         request.form['magnitude'])
    )
    conn.commit()
    conn.close()

    return redirect(url_for('Einterface.employee_view', empID=request.form['empID'], tab='EP', tab2='punc'))


@bp.route('/del_punctuality', methods=['POST'])
def del_punctuality():
    if session.get('managerID'):
        return redirect(url_for('Einterface.eview'))

    conn = db_connect()
    conn.execute(
        """DELETE FROM punctuality 
        WHERE empID=? AND incedent_date=?""",
        (request.form['empID'],
         request.form['incedent_date'])
    )
    conn.commit()
    conn.close()

    return redirect(url_for('Einterface.employee_view', empID=request.form['empID'], tab='EP', tab2='punc'))


@bp.route('/add_comments', methods=['POST'])
def add_comments():
    if session.get('managerID'):
        return redirect(url_for('Einterface.eview'))

    conn = db_connect()
    conn.execute(
        """INSERT INTO comments (empID, comments, magnitude)
        VALUES
            (?,?,?)""",
        (request.form['empID'],
         request.form['comments'],
         request.form['magnitude'])
    )
    conn.commit()
    conn.close()

    return redirect(url_for('Einterface.employee_view', empID=request.form['empID'], tab='EP', tab2='comm'))


@bp.route('/del_comments', methods=['POST'])
def del_comments():
    if session.get('managerID'):
        return redirect(url_for('Einterface.eview'))

    conn = db_connect()
    conn.execute(
        """DELETE FROM comments 
        WHERE empID=? AND comments=?""",
        (request.form['empID'],
         request.form['comments'])
    )
    conn.commit()
    conn.close()

    return redirect(url_for('Einterface.employee_view', empID=request.form['empID'], tab='EP', tab2='comm'))
