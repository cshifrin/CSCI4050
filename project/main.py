from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

import mysql.connector

app = Flask(__name__)

#Configure the application
app.config['MYSQL_HOST'] = 'localhost'
app.config['MTSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'BookStore'


####CONNECTOR CODE
userID = 12
addressID = 12
cardID = 12

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="BookStore"
)
mycursor=mydb.cursor()

regFormula = "INSERT INTO Users (User_ID, First_Name, Last_Name, Email, Cell_Phone, Password, Status, Receive_Promotion, User_Type_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

regAddressFormula = "INSERT INTO Addresses (User_ID, Address_ID, Street, City, State, Zip_Code) VALUES (%s, %s, %s, %s, %s, %s)"

regCardFormula = "INSERT INTO Payment_Cards (User_ID, Address_ID, Card_ID, Card_Number, Type_ID, Expiration_Date, Holder_Name) VALUES (%s, %s, %s, %s, %s, %s, %s)"



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
        cursor.execute('Select * FROM Users WHERE Email = %s AND Password = %s AND Status = 1', (inputEmail, inputPassword,))
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
    if request.method == 'POST' and 'inputName' in request.form and 'inputPhone' in request.form and 'inputEmail' in request.form and 'inputPassword' in request.form
    #and 'inputAddress' in request.form and 'inputCity' in request.form and 'inputState' in request.form and 'inputZip' in request.form and 'inputCardName' in request.form and 'inputCardNo' in request.form and 'inputCardDate' in request.form:
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
        
        #######	####Execute code to MySQL
	nameList = inputName.split()
	firstName = nameList[0]
	lastName = nameList[1]
	regInfo = (userID, firstName, lastName, inputEmail, inputPhone, inputPassword, 0, 0, 0)
	mycursor.execute(regFormula, regInfo)

	addInfo = (userID, addressID, inputAddress, inputCity, inputState, inputZip)
	mycursor.execute(regAddressFormula, addInfo)

	cardInfo = (userID, addressID, cardID, inputCardNo, 0, inputCardDate, inputCardName) 
	mycursor.execute(regCardFormula, cardInfo)

###DO WE NEED TO ADD A COUNTRY VARIABLE??
	
	mydb.commit()
	userID = userID+1
	addressID = addressID+1
	cardID = cardID +1

	####TODO////// --> We need to SEND CONFIRMATION EMAIL
	###TODO: Redirect to REGCON page. 
	return render_template('regcon.html')

    elif request.method == 'POST':
        msg = 'Please fill out ALL required fields.'
    return render_template('reg.html', msg=msg)

#######################################################################
########################     PASSWORD RESET     #######################
#######################################################################

