from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

#Create secret key
app.secret_key = 'key'

#Configure the application
app.config['MYSQL_HOST'] = 'localhost'
app.config['MTSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
ap.config['MYSQL_DB'] = 'BookStore'

mysql = MySQL(app)

#enable user to register
@app.route('/BookStore/', methods=['GET', 'POST'])
def login():
    return render_template('signin.html', msg='')

msg = 'Error'
#Check if "email" and "password" POST requests exist
if request.method == 'POST' and 'Email' in request.form and 'Password' in request.form:
    inputEmail4 = request.form['inputEmail4']
    inputPassword4 = request.form['inputPassword4']

#Check if account exists using MySQL
cursor = mysql.connection.cursor(MySQL.cursors.DictCursor)
cursor.execute('Select * FROM Users WHERE Email = %s AND Password = %s', (inputEmail4, inputPassword4,))
account = cursor.fetchone()


#Check if account exists using MySQL
cursor = mysql.connection.cursor(MySQL.cursors.DictCursor)
cursor.execute('SELECT * FROM Users WHERE Email = %s AND Password = %s', (inputEmail4, inputPassword4,))
account = cursor.fetchone()

#If account exists create session
#if account:
 #   return 'Logged in successfully.'
#else:
 #   msg = 'Incorrect email/password.'
  #  return msg
