from flask import Flask, flash, render_template, request, redirect, url_for, session, json
#from flask_mysqldb import MySQL
#import MySQLdb.cursors
import re
import smtplib, ssl
import random
from flaskext.mysql import MySQL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector

import base64
#from mysql import connector



### :) SQL Query Formulas, this time for the registerUser() function
regFormula = "INSERT INTO Users (User_ID, First_Name, Last_Name, Email, Cell_Phone, Password, Status, Recieve_Promotion, User_Type_ID, Conf_Code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
regAddressFormula = "INSERT INTO Addresses (User_ID, Address_ID, Street, City, State, Country, Zip_Code) VALUES (%s, %s, %s, %s, %s, %s, %s)"
regCardFormula = "INSERT INTO Payment_Cards (User_ID, Address_ID, Card_ID, Card_Number, Type_ID, Expiration_Date, Holder_Name) VALUES (%s, %s, %s, %s, %s, %s, %s)"


app = Flask(__name__)
#mysql = MySQL()

#Configure the application
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '#Hunter911'
app.config['MYSQL_DATABASE_DB'] = 'BookStore'
#mysql.init_app(app)

app.secret_key = 'key'


### :) :) :) CONNECTOR CODE for connector Driver

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="#Hunter911",
	database="BookStore"
)
mycursor=mydb.cursor()




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

#:) :) :) Get form data + match email/pass to DB, store into session.
    render_template('signin.html')
    if request.method == 'POST' and 'inputEmail' in request.form and 'inputPassword' in request.form:
        inputEmail = request.form['inputEmail']
        inputPassword = request.form['inputPassword']
        encPassword = base64.b64encode(inputPassword.encode("utf-8"))
        mycursor.execute('Select * FROM Users WHERE Email = %s AND Password = %s', (inputEmail, encPassword))
        data = mycursor.fetchone()
        email = str(data[3])
	
	#:) :) :) Store relevant info from DB into session
        if len(data) > 0:
#            if data[0][3] == encPassword:
                session['user'] = data[0]
                session['userEmail'] = email
                session['userType'] = data[8]

                if session['userType'] == 2:
                    #:) reg user
                    return redirect('/BookStore/userProfile')

                if session['userType'] == 3:
                    #:) admin
                    return redirect('/BookStore/adminProfile')


        else:
            flash('Invalid email/password.')
            return render_template('signin.html', msg = 'Invalid email/password.')
    else:
        flash('Invalid email/password.')
        return render_template('signin.html', msg='Invalid email/password.')

#ROUTES TO ADMINPROFILE PAGE
@app.route('/BookStore/adminprofile')
def adminprofile():
	return render_template('adminprofile.html')


#ROUTES TO USERPROFILE PAGE    
@app.route('/BookStore/userprofile')
def userprofile():
        return render_template('userprofile.html')

#SIGNOUT
#:) :)   pop the session variables
@app.route('/BookStore/signout')
def logout():
    session.pop('user',None)
    session.pop('userEmail',None)
    session.pop('userType',None)
#    flash('Logged out successfully!')
    msg='Logged out successfully!'
    return redirect('/')

#ROUTES TO REGISTRATION PAGE
@app.route('/BookStore/reg')
def viewReg():
    return render_template('reg.html')

#READS USER DATA FROM REGISTRATION PAGE
@app.route('/BookStore/reg', methods=['GET', 'POST'])
def reg():

#:) :) :) MY BABY! Pull all the form variables, input into dbs with relational logic
	if request.method == 'POST' and 'inputEmail' in request.form and 'inputName' in request.form and 'inputPhone' in request.form and 'inputPassword' in request.form:
		maxQuery = 'SELECT MAX(User_ID) FROM Users'
		mycursor.execute(maxQuery)
		maxID = mycursor.fetchone()
		maxID = int(''.join(map(str, maxID)))
		userID = maxID +1
		addressID = userID
		cardID = userID
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
		if 'inputCardDate' in request.form:
			inputCardDate = request.form['inputCardDate']
		else: 
			inputCardDate = None
		inputCountry = 'USA'
		firstName = ''
		lastName = ''

		encPassword = base64.b64encode(inputPassword.encode("utf-8"))
		encCardNo = base64.b64encode(inputCardNo.encode("utf-8"))

		nameList = inputName.split()
		if len(nameList) > 1:
			firstName = nameList[0]
			lastName = nameList[1]
		else:
			firstName = nameList[0]
		mycursor.execute('SELECT * FROM Users WHERE Email = %s', (inputEmail,))

		data = mycursor.fetchall()
		if len(data) > 0:
			flash('An account already exists under this email!')
			msg = 'An account already exists under this email!'
			return render_template('reg.html', msg=msg)
			
		regInfo = (userID, firstName, lastName, inputEmail, inputPhone, encPassword, 0, 0, 2, 0)
		mycursor.execute(regFormula, regInfo)
		mydb.commit()

		addInfo = (userID, addressID, inputAddress, inputCity, inputState, inputCountry, inputZip)
		mycursor.execute(regAddressFormula, addInfo)
		
		mydb.commit()

		cardInfo = (userID, addressID, cardID, encCardNo, 1, inputCardDate, inputCardName) 
		mycursor.execute(regCardFormula, cardInfo)
		
		mydb.commit()
		userID = userID+1
		addressID = addressID+1
		cardID = cardID +1

	### :) :)  :) send confirmation email	
		port = 465  # For SSL
		password = "@Bookstoreuga4050"

		smtp_server = "smtp.gmail.com"
		sender_email = "bookstoreuga4050@gmail.com"
		receiver_email = inputEmail
		code = random.randint(1000, 9999)
		code = str(code)
		#print(code)
		message = """\ Subject: Hi, your code is 
	
		%s
		""" % code

		# Create a secure SSL context
		context = ssl.create_default_context()
	
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login("bookstoreuga4050@gmail.com", password)
			server.sendmail(sender_email, receiver_email, message)
	### :) :) :) email sent
		mycursor.execute('UPDATE Users SET Conf_Code = %s WHERE Email = %s', (code, inputEmail))
		mydb.commit()

	### :) :) :) code stored in DB, now redirect to regcon page
		return redirect('/regcon')

	elif request.method == 'POST':
		flash('Please fill out ALL required fields.')
		msg = 'Please fill out ALL required fields.'
		return render_template('reg.html', msg=msg)     

#ROUTES TO REGCON PAGE    
@app.route('/regcon')
def regcon():
    return render_template('regcon.html')


@app.route('/regcon', methods=['GET','POST'])
### :) :) this method is to confirm registration; users must enter a code that was sent to their email.
def confirm():
	if request.method == 'POST':
		inputCode = request.form['confNum']		
		inputEmail = request.form['inputEmail']
		
		mycursor.execute('SELECT Conf_Code FROM Users WHERE Email = %s', (inputEmail,))
		code = mycursor.fetchone()
		code = int(''.join(map(str, code)))		
		

		### :) set status from 0 (inactive) to 1 (active)
		newStatus = ("1", inputEmail)
		statusFormula = "UPDATE Users SET Status = %s WHERE Email = %s"

		### :) check if codes are equal
		if int(inputCode) == code: 
			mycursor.execute(statusFormula, newStatus)

			mydb.commit()
			return redirect('/BookStore/signin')
		else: 
			flash('Incorrect code or incorrect email, please try again.')
			return render_template('regcon.html')


#ROUTES TO HOME
@app.route('/BookStore/home')
def home(): 
    return render_template('home.html')

@app.route('/BookStore/forgotpwd')
def view():
    return render_template('forgotpwd.html')

@app.route('/BookStore/forgotpwd', methods=['POST'])
def resetPwd():
    msg=''
    if request.method == 'POST' and 'emailFP' in request.form:
        emailFP = request.form['emailFP']
        mycursor.execute('Select * FROM Users WHERE Email = %s', (emailFP,))
        user = mycursor.fetchone()
        if len(user) > 0:
            port = 465  # For SSL
            password = "@Bookstoreuga4050"
            smtp_server = "smtp.gmail.com"
            sender_email = "bookstoreuga4050@gmail.com"
#:) :) :) Use user session email to retrieve email to send forgotpwd
        #mycursor.execute('SELECT * FROM Users WHERE Email = %s', (session['userEmail'],))

            receiver_email = emailFP
            code = random.randint(1000, 9999)
            code = str(code)
            #print(code)
            message = """\ Subject: Hi, your code is 
            %s
            """ % code

    # Create a secure SSL context
    # :) :) :) Send the emails
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login("bookstoreuga4050@gmail.com", password)
                server.sendmail(sender_email, receiver_email, message)
            mycursor.execute('UPDATE Users SET Conf_Code = %s WHERE Email = %s', (code, emailFP))
            mydb.commit()

            return redirect('/BookStore/viewChangePwd')
        else:
            msg = 'Invalid email. Try again.'
            return redirect('/BookStore/forgotpwd')

#ROUTES TO CHANGE PASSWORD PAGE
@app.route('/BookStore/viewChangePwd')
def viewChangePwd():
    return render_template('changepwd.html')

#READS DATA FROM CHANGE PASSWORD PAGE
@app.route('/BookStore/viewChangePwd', methods=['GET', 'POST'])
def changePwd():
        ########TRIGGER PASSWORD RESET#######
    #currentpwd = "password"
    #current = input("To change password, enter current password: ")
    #if current == currentpwd:

    if request.method == 'POST' and 'codeFP' in request.form and 'newPass' in request.form and 'confirmPass' in request.form:
        inputEmail = request.form['inputEmail']
        codeFP = request.form['codeFP']
        newPass = request.form['newPass']
        confirmPass = request.form['confirmPass']

        passFormula = "UPDATE Users SET Password = %s WHERE Email = %s"
    
	### :) check if codes are equal
        mycursor.execute('SELECT Conf_Code FROM Users WHERE Email = %s', (inputEmail,))
        code = mycursor.fetchone()
        code = int(''.join(map(str, code)))		

        encPassword = base64.b64encode(newPass.encode("utf-8"))
        if int(codeFP) == code and newPass==confirmPass: 
            mycursor.execute(passFormula, (encPassword, inputEmail))
            mydb.commit()

            msg = 'Password changed successfully.'
            return redirect('/BookStore/signin')
        else:
            msg = 'Passwords or code do not match. Try again.'
            return redirect('/BookStore/viewChangePwd')
    else:
        msg = 'Please fill out all fields.'
        return redirect('/BookStore/viewChangePwd')
        #change password
    
    #if confirmation == code: 
    #    if newPassword == newConf: 
    #        mycursor.execute(passFormula, newPass)
    #        mydb.commit()

    #return render_template('changepwd.html', msg='')

#ROUTES TO EDIT PROFILE PAGE
@app.route('/BookStore/editprofile')
def viewEditProfile():
    if session['user'] == None:
        return redirect('/')
    else:
        return render_template('editprofile.html')

#READS DATA FROM EDIT PROFILE PAGE
@app.route('/BookStore/editprofile', methods = ['GET', 'POST'])
def editprofile():

#:) Similar input fields as register, but updating profile
	msg = ''
	if request.method == 'POST' and 'inputName' in request.form and 'inputPhone' in request.form and 'inputPassword' in request.form:
		#we know that session['userEmail'] has our email. 
#		maxQuery = 'SELECT MAX(User_ID) FROM Users'
#		mycursor.execute(maxQuery)
#		maxID = mycursor.fetchone()
#		maxID = int(''.join(map(str, maxID)))
#		userID = maxID +1
#		addressID = userID
#		cardID = userID

### :) :) :) a new fnc to pull the data from database using credentials in login session
		mycursor.execute('SELECT * FROM Users WHERE Email = %s', (session['userEmail'],))
		data = mycursor.fetchone()
		
		userID = data[0]
		

		##TODO: update maxQUery to currentUserQuery

		inputName = request.form['inputName']
		inputPhone = request.form['inputPhone']
		inputPassword = request.form['inputPassword']
		inputAddress = request.form['inputAddress']
		inputCity = request.form['inputCity']
		inputState = request.form['inputState']
		inputZip = request.form['inputZip']
		inputCardName = request.form['inputCardName']
		inputCardNo = request.form['inputCardNo']
		inputCardDate = request.form['inputCardDate']
		nameList = inputName.split()
		firstName = nameList[0]
		lastName = nameList[1]

		encPassword = base64.b64encode(inputPassword.encode("utf-8"))
		encCardNo = base64.b64encode(inputCardNo.encode("utf-8"))


	### :) :) :) Store data from form as tuples to push into SQL Queries.

		newFirstName = (firstName, userID)
		newLastName = (lastName, userID)
		cell = (inputPhone, userID)
		newPass = (encPassword, userID)

		addr = (inputAddress, userID)
		city = (inputCity, userID)
		state = (inputState, userID)
		country = ("USA", userID)
		zip = (inputZip, userID)

		num = (inputCardName, userID)
		exp = (encCardNo, userID)
		name = (inputCardDate, userID)


		### :) :) :) about to have a bunch of SQL formulas and executions! 
		#editFormula = "UPDATE Users SET (First_Name, Last_Name, Cell_Phone, Password) WHERE 

		editNameFormula = "UPDATE Users SET First_Name = %s WHERE User_ID = %s"
		editLNameFormula = "UPDATE Users SET Last_Name = %s WHERE User_ID = %s"
		editPhoneFormula = "UPDATE Users SET Cell_Phone = %s WHERE User_ID = %s"
		editPassFormula = "UPDATE Users SET Password = %s WHERE User_ID = %s"

		mycursor.execute(editNameFormula, newFirstName)
		mycursor.execute(editLNameFormula, newLastName)
		mycursor.execute(editPhoneFormula, cell)
		mycursor.execute(editPassFormula, newPass)
	
	### :) :) :) Input Addr data :)

		editAddrFormula = "UPDATE Addresses SET Street = %s WHERE User_ID = %s"
		editCityFormula = "UPDATE Addresses SET City = %s WHERE User_ID = %s"
		editStateFormula = "UPDATE Addresses SET State = %s WHERE User_ID = %s"
		editCountryFormula = "UPDATE Addresses SET Country = %s WHERE User_ID = %s"
		editZipFormula = "UPDATE Addresses SET Zip_Code = %s WHERE User_ID = %s"


		mycursor.execute(editAddrFormula, addr)
		mycursor.execute(editCityFormula, city)
		mycursor.execute(editStateFormula, state)
		mycursor.execute(editCountryFormula, country)
		mycursor.execute(editZipFormula, zip)

	### :) :) :) INPUT CARD DATA

		editNumFormula = "UPDATE Payment_Cards SET Card_Number = %s WHERE User_ID = %s"
		editExpFormula = "UPDATE Payment_Cards SET Expiration_Date = %s WHERE User_ID = %s"
		editNameFormula = "UPDATE Payment_Cards SET Holder_Name = %s WHERE User_ID = %s"

		mycursor.execute(editNumFormula, num)
		mycursor.execute(editExpFormula, exp)
		mycursor.execute(editNameFormula, name)

		mydb.commit()
		flash('Edited Profile successfully! Your changes have been saved')
		
##TODO :) :) :) 
	#add email notification, if possible. 
		return render_template('userprofile.html', msg='Logged in successfully!')
	else:
		return redirect('/editprofile')


### Other routing :)



#ROUTES TO UNREGSEARCH PAGE
@app.route('/BookStore/unregsearch')
def viewunregsearch():
    ####if user == active, route to search.html
    ####else, route to unregsearch.html
    return render_template('unregsearch.html')

#READS DATA FROM UNREGSEARCH PAGE
@app.route('/BookStore/unregsearch', methods = ['GET', 'POST'])
def unregsearch():
    return

#ROUTES TO SEARCH PAGE
@app.route('/BookStore/search')
def viewsearch():
    ####if user == active, route to search.html
    ####else, route to unregsearch.html
    return render_template('search.html')

#READS DATA FROM SEARCH PAGE
@app.route('/BookStore/search', methods = ['GET', 'POST'])
def search():
    return

#ROUTES TO UNREGBOOKDETAILS PAGE
@app.route('/BookStore/unregbookdetails')
def viewunregbookdetails():
    return render_template('unregbookdetails.html')

#ROUTES TO BOOKDETAILS PAGE
@app.route('/BookStore/bookdetails')
def viewbookdetails():
    return render_template('bookdetails.html')

#ROUTES TO CHECKOUT PAGE
@app.route('/BookStore/checkout')
def viewcheckout():
    return render_template('checkout.html')

#READS DATA FROM CHECKOUT PAGE
@app.route('/BookStore/checkout', methods = ['GET', 'POST'])
def checkout():
    return

#ROUTES TO CHECKOUT PAGE
@app.route('/BookStore/checkoutcon')
def viewcheckoutcon():
    return render_template('checkoutcon.html')

#ROUTES TO ORDERCON PAGE
@app.route('/BookStore/ordercon')
def viewordercon():
    return render_template('ordercon.html')

#ROUTES TO CART PAGE
@app.route('/BookStore/cart')
def viewcart():
    return render_template('cart.html')

#ROUTES TO ORDERHISTORY PAGE
@app.route('/BookStore/orderhistory')
def vieworderhistory():
    return render_template('orderhistory.html')

#ROUTES TO ORDERHISTORY PAGE
@app.route('/BookStore/bookreturn')
def viewbookreturn():
    return render_template('bookreturn.html')

#ROUTES TO MANAGEBOOKS PAGE
@app.route('/BookStore/managebooks')
def viewmanagebooks():
    return render_template('managebooks.html')

#READS DATA FROM MANAGEBOOKS PAGE
@app.route('/BookStore/managebooks', methods = ['GET', 'POST'])
def managebooks():
    ####For edit books
    if request.method == 'POST' and 'inputSearchManage' in request.form:
        inputSearchManage = request.form['inputSearchManage']
        mycursor.execute('Select * FROM Books WHERE Book_ID = %s', (inputSearchManage,))
        book = mycursor.fetchone()
        if len(book) == 0:
            flash('Book does not exist.')
            msg = 'Book does not exist.'
            return redirect('/BookStore/viewmanagebooks')
        else:
            ###edit books###
            return
            
    ####For add books    
    elif request.method == 'POST' and 'inputBookID' in request.form:
            inputBookID = request.form['inputBookID']
            mycursor.execute('Select * FROM Books WHERE Book_ID = %s', (inputBookID,))
            book = mycursor.fetchone()
            if len(book) > 0:
                flash('Book already exists.')
                msg = 'Book already exists.'
                return redirect('/BookStore/viewmanagebooks')
            else:
                inputTitle = request.form['inputTitle']
                inputAuthor = request.form['inputAuthor']
                inputPrice = request.form['inputPrice']
                inputPublisher = request.form['inputPublisher']
                inputSubject = request.form['inputSubject']
                bookFormula = "INSERT INTO Books (Title, Publisher_ID, Author, Book_ID) VALUES (%s, %s, %s, %s)"
                bookInfo = (inputTitle, inputPublisher, inputAuthor, inputBookID)
                mycursor.execute(bookFormula, bookInfo)
                mydb.commit()
                return redirect('/BookStore/viewmanagebooks')
    else:
        return redirect('/BookStore/viewmanagebooks')
        


#MAIN METHOD
if __name__=="__main__":
	app.run(port=8000, debug=True)
