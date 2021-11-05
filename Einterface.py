from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from db import *


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

    db = db_connect()
    total = db.execute(
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

    top = {}
    top['projects'] = db.execute(
        """SELECT c.empID, SUM(magnitude) as mag_sum, fname, lname
        FROM completed_projects c
        JOIN employees e ON e.empID = c.empID
        GROUP BY c.empID
        ORDER BY msum DESC""",
    ).fetchmany(5)

    top['comments'] = db.execute(
        """SELECT c.empID, SUM(magnitude) as mag_sum, fname, lname
        FROM comments c
        JOIN employees e ON e.empID = c.empID
        GROUP BY c.empID
        ORDER BY msum DESC""",
    ).fetchmany(5)

    db_close()
    return render_template('Einterface/elanding.html', total, top)