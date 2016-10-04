# coding: utf-8
# import common modules #
import sys, os
from flask import Flask, request, redirect, render_template, url_for
import numpy as np

# import my modules #
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/calc/market')
#import fuel_price

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

# index
@app.route('/')
def index():
    title = project_name
    return render_template('index.html', title=title)

# Login
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

#### Ship Performance ####
@app.route('/performance')
def ship_performance():
    return render_template('ship_model')

##### Market #####
@app.route('/market')
def market():
    HistoryExcel = ''
    date, dataCO, dataNG  = fuel_price.history_data(HistoryExcel)
    return render_template('market.html', result=zip(date, dataCO, dataNG))

##### Route #####


# main
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
