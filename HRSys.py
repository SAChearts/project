'''from flask import *
from db import *

app = Flask(__name__)
@app.route('/login')
def loginMain():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    login(username,password)
'''
