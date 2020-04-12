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

#enable user to register
@app.route('/BookStore/', methods=['GET', 'POST'])
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
            return 'Logged in successfully.'
        else:
            msg = 'ERROR'
    return render_template('home.html', msg=msg)

#If account exists create session
#if account:
 #   return 'Logged in successfully.'
#else:
 #   msg = 'Incorrect email/password.'
  #  return msg
