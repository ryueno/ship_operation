import os
import sys
from flask import Flask, request, redirect, render_template, url_for

project_name = 'Ship Operation Simulation'
error_message = 'invalid error, try again'

app = Flask(__name__)

app.config.update(dict(
    #DATABASE=os.path.join(app.root_path, ''),
    #SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='hogehoge'
))
app.config.from_envvar('SHIP_OPERATION_SETTINGS', silent=True)

@app.route('/')
def index():
    title = project_name
    return render_template('index.html', title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        if request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
