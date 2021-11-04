from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
#from werkzeug.exceptions import abort

#from flaskr.auth import login_required
#from flaskr.db import get_db

bp = Blueprint('Einterface', __name__)
@bp.route('/')
def home():
    #Under construction 
    return render_template('Einterface/home.html')

@bp.route('/eview')
def eview():
    #under construction
    return render_template('Einterface/elanding.html')
