from flask import Flask, render_template, request, redirect, url_for, session, json
#from flask_mysqldb import MySQL
#import MySQLdb.cursors
import re
import smtplib, ssl
import random
import mysql.connector
from python_mysql_dbconfig import read_db_config
from flaskext.mysql import MySQL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#import mysql.connector
#from mysql import connector

app = Flask(__name__)
mysql = MySQL()

#Configure the application
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '#Hunter911'
app.config['MYSQL_DATABASE_DB'] = 'BookStore'
mysql.init_app(app)

app.secret_key = 'key'

####CONNECTOR CODE

#mydb = mysql.connector.connect(
#	host="localhost",
#	user="root",
#	passwd="#Hunter911",
#	database="BookStore"
#)

mycursor=mydb.cursor()

userID = 18
addressID = 18
cardID = 18

regFormula = "INSERT INTO Users (User_ID, First_Name, Last_Name, Email, Cell_Phone, Password, Status, Receive_Promotion, User_Type_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

regAddressFormula = "INSERT INTO Addresses (User_ID, Address_ID, Street, City, State, Country, Zip_Code) VALUES (%s, %s, %s, %s, %s, %s, %s)"

regCardFormula = "INSERT INTO Payment_Cards (User_ID, Address_ID, Card_ID, Card_Number, Type_ID, Expiration_Date, Holder_Name) VALUES (%s, %s, %s, %s, %s, %s, %s)"



#mysql = MySQL(app)


#STARTS OUT AT HOME
@app.route("/")
def main():
    return render_template('home.html')

#ROUTES TO SIGNIN PAGE
@app.route('/BookStore/signin')
def viewSignin():
    return render_template('signin.html')

#READS USER DATA FROM SIGNIN PAGE
@app.route('/BookStore/signin', methods=['POST'])
def signin():
    render_template('signin.html')
    if request.method == 'POST' and 'inputEmail' in request.form and 'inputPassword' in request.form:
        inputEmail = request.form['inputEmail']
        inputPassword = request.form['inputPassword']

        con = mysql.connect()
        cursor = con.cursor()
        #Check for user
        cursor.execute('Select * FROM Users WHERE Email = %s AND Password = %s', (inputEmail, inputPassword))
        data = cursor.fetchall()
        if len(data) > 0:
            if data[0][3] == _password:
                session['user'] = data[0][0]
                return redirect('/userProfile')
            else:
                return render_template('signin.html', msg = 'Invalid email/password.')
        else:
            return render_template('signin.html', msg = 'Invalid email/password.')
    else:
        return render_template('signin.html', msg='Invalid email/password.')

#ROUTES TO USERPROFILE PAGE    
@app.route('/BookStore/userProfile')
def userProfile():
        return render_template('userprofile.html')

#LOGOUT    
@app.route('/BookStore/logout')
def logout():
    session.pop('user',None)
    return redirect('/')

#ROUTES TO REGISTRATION PAGE
@app.route('/BookStore/reg')
def viewReg():
    return render_template('reg.html')

#READS USER DATA FROM REGISTRATION PAGE
@app.route('/BookStore/reg', methods=['GET', 'POST'])
def reg():
    msg = ''
    if request.method == 'POST' and 'inputName' in request.form and 'inputPhone' in request.form and 'inputEmail' in request.form and 'inputPassword' in request.form:
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
	inputCountry = 'USA'
	#EXECUTE CODE TO MYSQL
	nameList = inputName.split()
	firstName = nameList[0]
	lastName = nameList[1]
        
	regInfo = (userID, firstName, lastName, inputEmail, inputPhone, inputPassword, 0, 0, 2)
	mycursor.execute(regFormula, regInfo)
	addInfo = (userID, addressID, inputAddress, inputCity, inputState, inputCountry, inputZip)
	mycursor.execute(regAddressFormula, addInfo)
	cardInfo = (userID, addressID, cardID, inputCardNo, 0, inputCardDate, inputCardName) 
	mycursor.execute(regCardFormula, cardInfo)
        
	mydb.commit()
	userID = userID+1
	addressID = addressID+1
	cardID = cardID +1
        
	confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
	confirm_url = url_for('users.confirm_email', 
	token=confirm_serializer.dumps(inputEmail, salt='email-confirmation-salt'),
	_external=True)
	html = render_template('emailContent.html')
                               #confirm_url=confirm_url)
        
	send_email('Confirm Your Email Address', [inputEmail], html)
	flash('Thanks for registering! Please confirm your account by finding the message sent to your email address.', 'success')

        return redirect('/regcon')

    elif request.method == 'POST':
       	msg = 'Please fill out ALL required fields.'
	return render_template('reg.html')     

    if request.method == 'POST' and 'inputEmail' in request.form and 'inputPassword' in request.form:
        inputEmail = request.form['inputEmail']
        inputPassword = request.form['inputPassword']

        #Check if account exists using MySQL
        #cursor = mysql.connection.cursor(MySQL.cursors.DictCursor)
        mycursor.execute('Select * FROM Users WHERE Email = %s AND Password = %s AND Status = 1', (inputEmail, inputPassword,))
        user = mycursor.fetchone()

        #Check if account exists in database
        if user:
            session['loggedin'] = True
            session['inputEmail'] = user['inputEmail']
            session['inputPassword'] = user['inputPassword']
            return render_template('userprofile.html')
        else:
            msg = 'Incorrect username/password.'
            return render_template('signin.html')
    else:
        return redirect('/reg')

#ROUTES TO REGCON PAGE    
@app.route('/BookStore/regcon')
def regcon():
    return render_template('regcon.html')

#ROUTES TO HOME
@app.route('/BookStore/home')
def home(): 
    return render_template('home.html')

#ROUTES TO FORGOT PASSWORD PAGE
@app.route('/BookStore/forgotpwd')
def viewForgotPwd():
    return render_template('forgotpwd.html')

#READS DATA FROM FORGOT PASSWORD PAGE
@app.route('/BookStore/forgotpwd', methods=['GET', 'POST'])
def resetPwd():
    msg=''
    if request.method == 'POST' and 'emailFP' in request.form:
        emailFP = request.form['emailFP']
        mycursor.execute('Select * FROM Users WHERE Email = %s', (emailFP))
        user = mycursor.fetchone()
        if user:
            return redirect('/viewChangePwd')
        else:
            msg = 'Invalid email. Try again.'
            return redirect('/viewForgotPwd')

#ROUTES TO CHANGE PASSWORD PAGE
@app.route('/BookStore/changepwd')
def viewChangePwd():
    return render_template('changepwd.html')

#READS DATA FROM CHANGE PASSWORD PAGE
@app.route('/BookStore/changepwd', methods=['GET', 'POST'])
def changePwd():
    port = 465  # For SSL
    password = "@Bookstoreuga4050"
    smtp_server = "smtp.gmail.com"
    sender_email = "bookstoreuga4050@gmail.com"
    receiver_email = "alt07134@uga.edu"
    code = random.randint(1000, 9999)
    code = str(code)
    #print(code)
    message = """\ Subject: Hi, your code is 
    %s
    """ % code
    ########TRIGGER PASSWORD RESET#######
    #currentpwd = "password"
    #current = input("To change password, enter current password: ")
    #if current == currentpwd:
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login("bookstoreuga4050@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)

    if request.method == 'POST' and 'inputEmail' in request.form and 'codeFP' in request.form and 'newPass' in request.form and 'confirmPass' in request.form:
        inputEmail = request.form['inputEmail']
        codeFP = request.form['codeFP']
        newPass = request.form['newPass']
        confirmPass = request.form['confirmPass']
        if newPass == confirmPass and codeFP == code:
            db_config = read_db_config()
            query = """UPDATE Users
            SET Password = %s
            WHERE Email = %s"""
            data = (newPass, inputEmail)
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            msg = 'Password changed successfully.'
            return rendirect('/viewSignIn')
        else:
            msg = 'Passwords or code do not match. Try again.'
            return redirect('/viewChangePwd')
    else:
        msg = 'Please fill out all fields.'
        return redirect('/viewChangePwd')
        #change password
    #newPass = (newConf, userID)
    #passFormula = "UPDATE Users SET Password = %s WHERE User_ID = %s"
    
    #if confirmation == code: 
    #    if newPassword == newConf: 
    #        mycursor.execute(passFormula, newPass)
    #        mydb.commit()

    #return render_template('changepwd.html', msg='')

#ROUTES TO EDIT PROFILE PAGE
@app.route('/BookStore/editprofile')
def viewEditProfile():
    return render_template('editprofile.html')

#READS DATA FROM EDIT PROFILE PAGE
@app.route('/BookStore/editprofile')
def editprofile():
    msg = ''
    if request.method == 'POST' and 'inputName' in request.form and 'inputPhone' in request.form and 'inputPassword' in request.form:
	inputName = request.form['inputName']
	inputPhone = request.form['inputPhone']
	inputEmail = request.form['inputEmail']
	inputPassword = request.form['inputPassword']
	inputAddress = request.form['inputAddress']
	inputCity = request.form['inputCity']
	inputState = request.form['inputState']
	inputZip = request.form['inputZip']
	inputCardName = request.form['inputCardName']
	inputCardNo = request.form['inputCardNo']
	inputCardDate = request.form['inputCardDate']
               
        #EXECUTE CODE TO MYSQL
	print(inputName + ' ' + inputPhone + ' ' + inputEmail)
	nameList = inputName.split()
	firstName = nameList[0]
	lastName = nameList[1]
	regInfo = (userID, firstName, lastName, inputEmail, inputPhone, inputPassword, 0, 0, 2)
	mycursor.execute(regFormula, regInfo)
        
	addInfo = (userID, addressID, inputAddress, inputCity, inputState, inputCountry, inputZip)
	mycursor.execute(regAddressFormula, addInfo)

	cardInfo = (userID, addressID, cardID, inputCardNo, 0, inputCardDate, inputCardName) 
	mycursor.execute(regCardFormula, cardInfo)
	mycursor.commit()
	
	msg = 'Profile was updated.'
	return render_template('userprofile.html', msg=msg)
    else:
        return redirect('/editprofile')

#def logout():
	#wtf what triggers a logout function
#    session.pop('loggedin', None)
#    session.pop('id', None)
#    session.pop('username', None)
#    return render_template('signin.html', msg='')

#MAIN METHOD
if __name__=="__main__":
	app.run(port=8000, debug=True)
