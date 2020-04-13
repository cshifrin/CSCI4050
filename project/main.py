from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

#Configure the application
app.config['MYSQL_HOST'] = 'localhost'
app.config['MTSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'BookStore'

mysql = MySQL(app)

#######################################################################
##########################     LOGIN     ##############################
#######################################################################
@app.route('/BookStore/Users', methods=['GET', 'POST'])
def login():
    return render_template('signin.html', msg='')
    msg = ''
    #Check if "email" and "password" POST requests exist
    if request.method == 'POST' and 'inputEmail' in request.form and 'inputPassword' in request.form:
        inputEmail = request.form['inputEmail']
        inputPassword = request.form['inputPassword']

        #Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQL.cursors.DictCursor)
        cursor.execute('Select * FROM Users WHERE Email = %s AND Password = %s', (inputEmail, inputPassword,))
        user = cursor.fetchone()


        #Check if account exists in database
        if account:
            session['loggedin'] = True
            session['inputEmail'] = user['inputEmail']
            session['inputPassword'] = user['inputPassword']
            return render_template('userprofile.html', msg='')
        else:
            msg = 'Incorrect username/password.'
            return render_template('signin.html', msg=msg)
        
######################################################################
############################    LOGOUT    ############################
######################################################################
@app.route('/BookStore/Users')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return render_template('signin.html', msg='')
        
######################################################################
#####################      REGISTRATION     ##########################
######################################################################
@app.route('/BookStore/Users', methods=['GET', 'POST'])
def register():
    return render_template('reg.html', msg='')
    msg = ''
    if request.method == 'POST' and 'inputName' in request.form and 'inputPhone' in request.form and 'inputEmail' in request.form and 'inputPassword' in request.form and 'inputAddress' in request.form and 'inputCity' in request.form and 'inputState' in request.form and 'inputZip' in request.form and 'inputCardName' in request.form and 'inputCardNo' in request.form and 'inputCardDate' in request.form:
        inputName = request.form['inputName']
        inputPhone = request.form['inputPhone']
        inputEmail = request.form['inputEmail']
        inputPassword = request.form['inputPassword']
        inputAddress = request.form['inputAddress']
        inputCity = request.form['inputCity']
        inputState = request.form['inputstate']
        inputZip = request.form['inputZip']
        inputCardName = request.form['inputCardName']
        inputCardNo = request.form['inputCardNo']
        inputCardDate = request.form['inputCardDate']
    elif request.method == 'POST':
        msg = 'Please fill out ALL required fields.'
    return render_template('reg.html', msg=msg)

#######################################################################
########################     PASSWORD RESET     #######################
#######################################################################

