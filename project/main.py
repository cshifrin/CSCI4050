#CS4050-8

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
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
##app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
#app.config['MYSQL_DATABASE_DB'] = 'BookStore'
#mysql.init_app(app)

app.secret_key = 'key'


### :) :) :) CONNECTOR CODE for connector Driver

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="password",
	database="BookStore"
)
mycursor=mydb.cursor()


#mysql = MySQL(app)


#STARTS OUT AT HOME
@app.route("/")
def main():

    return render_template('home.html')

@app.route("/BookStore/")
def bookstore():
    return render_template('home.html')

#ROUTES TO SIGNIN PAGE
@app.route('/BookStore/signin/')
def viewSignin():
    return render_template('signin.html')

#READS USER DATA FROM SIGNIN PAGE
@app.route('/BookStore/signin/', methods=['POST'])
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
                    resetCart = "DELETE FROM cart;"
                    mycursor.execute(resetCart)
                    mydb.commit()
                    return redirect('/BookStore/userprofile')

                if session['userType'] == 3:
                    #:) admin
                    return redirect('/BookStore/adminprofile')


        else:
            flash('Invalid email/password.')
            return render_template('signin.html', msg = 'Invalid email/password.')
    else:
        flash('Invalid email/password.')
        return render_template('signin.html', msg='Invalid email/password.')

#ROUTES TO ADMINPROFILE PAGE
@app.route('/BookStore/adminprofile/')
def adminprofile():
	return render_template('adminprofile.html')


#ROUTES TO USERPROFILE PAGE    
@app.route('/BookStore/userprofile/')
def userprofile():
        return render_template('userprofile.html')

#SIGNOUT
#:) :)   pop the session variables
@app.route('/BookStore/signout/')
def logout():
    session.pop('user',None)
    session.pop('userEmail',None)
    session.pop('userType',None)
#    flash('Logged out successfully!')
    msg='Logged out successfully!'

    resetCart = "DELETE FROM cart;"
    mycursor.execute(resetCart)
    mydb.commit()

    return redirect('/')

#ROUTES TO REGISTRATION PAGE
@app.route('/BookStore/reg/')
def viewReg():
    return render_template('reg.html')

#READS USER DATA FROM REGISTRATION PAGE
@app.route('/BookStore/reg/', methods=['GET', 'POST'])
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
@app.route('/regcon/')
def regcon():
    return render_template('regcon.html')


@app.route('/regcon/', methods=['GET','POST'])
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
@app.route('/BookStore/home/')
def home(): 
    return render_template('home.html')

@app.route('/BookStore/forgotpwd/')
def view():
    return render_template('forgotpwd.html')

@app.route('/BookStore/forgotpwd/', methods=['POST'])
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
@app.route('/BookStore/viewChangePwd/')
def viewChangePwd():
    return render_template('changepwd.html')

#READS DATA FROM CHANGE PASSWORD PAGE
@app.route('/BookStore/viewChangePwd/', methods=['GET', 'POST'])
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
            return redirect('/BookStore/signin/')
        else:
            msg = 'Passwords or code do not match. Try again.'
            return redirect('/BookStore/viewChangePwd/')
    else:
        msg = 'Please fill out all fields.'
        return redirect('/BookStore/viewChangePwd/')
        #change password
    
    #if confirmation == code: 
    #    if newPassword == newConf: 
    #        mycursor.execute(passFormula, newPass)
    #        mydb.commit()

    #return render_template('changepwd.html', msg='')

#ROUTES TO EDIT PROFILE PAGE
@app.route('/BookStore/editprofile/')
def viewEditProfile():
    if session['user'] == None:
        return redirect('/')
    else:
        return render_template('editprofile.html')

#READS DATA FROM EDIT PROFILE PAGE
@app.route('/BookStore/editprofile/', methods = ['GET', 'POST'])
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
		return redirect('/editprofile/')


### Other routing :)


@app.route('/BookStore/search/', methods=['GET', 'POST'])
def search():
    if request.method == "GET":
        return render_template('search.html')

    if request.method == "POST":
        book = request.form['inputSearch']
        # search by author or book
        mycursor.execute("SELECT Title, Author, Price, Subject, Book_ID FROM Books WHERE Title LIKE %s OR Author LIKE %s OR Subject LIKE %s", (book, book, book))
        data = mycursor.fetchall()
        print(data)
        return render_template('search.html', data=data)
    return render_template('search.html')

@app.route('/BookStore/unregsearch/', methods=['GET', 'POST'])
def unregsearch():
    if request.method == "POST":
        book = request.form['inputSearch']
        # search by author or book
        mycursor.execute("SELECT Title, Author, Price, Subject, Book_ID from Books WHERE Title LIKE %s OR Author LIKE %s OR Subject LIKE %s", (book, book, book))
        data = mycursor.fetchall()
        # all in the search box will return all the tuples
#        if len(data) == 0 and book == 'all': 
#            mycursor.execute("SELECT Title, Author, Subject, Book_ID from Books")
#            mydb.commit()
#            data = mycursor.fetchall()
        return render_template('unregsearch.html', data=data)
    return render_template('unregsearch.html')

#ROUTES TO UNREGBOOKDETAILS PAGE
@app.route('/BookStore/unregbookdetails/')
def viewunregbookdetails():
    return render_template('unregbookdetails.html')


#ROUTES TO CHECKOUT PAGE
@app.route('/BookStore/checkout/')
def viewcheckout():
    mycursor.execute("SELECT Title, Author, Price, Subject, Book_ID FROM cart")
    bookData = mycursor.fetchall()

    #get price
    mycursor.execute("SELECT SUM(Price) FROM cart")
    price = mycursor.fetchall()
    price = "{:.2f}".format(price[0][0])

    if len(bookData) > 0:
        return render_template('checkout.html', data=bookData, price=price)
    else:
        return redirect('/BookStore/search/')

#READS DATA FROM CHECKOUT PAGE
@app.route('/BookStore/checkout/', methods = ['GET', 'POST'])
def checkout():
    return

#ROUTES TO CHECKOUT PAGE
@app.route('/BookStore/checkoutcon/', methods=['GET', 'POST'])
def viewcheckoutcon():
    if request.method == "POST":
        promoCode = request.form['inputPromotion']

        mycursor.execute("SELECT Title, Author, Price, Subject, Book_ID FROM cart")
        bookData = mycursor.fetchall()

        #get price
        mycursor.execute("SELECT SUM(Price) FROM cart")
        price = mycursor.fetchall()
        price = price[0][0]

        sub = price

        percent = 0

        if promoCode != "None":
            mycursor.execute("SELECT Percentage FROM Promotions WHERE Promotions_ID = %s", (promoCode,))
            data = mycursor.fetchall()
            #print(data)
            if len(data) > 0:
                percent = data[0][0]

        prom = (float(price) * float(float(percent) / 100))
        price = float(price) - prom
        tax = float(price) * .06

        price += tax

        return render_template('checkoutcon.html', data=bookData, price="{:.2f}".format(price), prom="{:.2f}".format(prom), tax="{:.2f}".format(tax), sub="{:.2f}".format(sub))

#ROUTES TO ORDERCON PAGE
@app.route('/BookStore/ordercon/')
def viewordercon():
    resetCart = "DELETE FROM cart;"
    mycursor.execute(resetCart)
    mydb.commit()
    return render_template('ordercon.html')


#ROUTES TO ORDERHISTORY PAGE
@app.route('/BookStore/orderhistory/')
def vieworderhistory():
    return render_template('orderhistory.html')

#ROUTES TO ORDERHISTORY PAGE
@app.route('/BookStore/bookreturn/')
def viewbookreturn():
    return render_template('bookreturn.html')

#ROUTES TO MANAGEBOOKS PAGE
#@app.route('/BookStore/managebooks')
#def viewmanagebooks():
#    return render_template('managebooks.html')

#ROUTES TO ADD BOOK PAGE
@app.route('/BookStore/addbook/')
def viewaddbook():
    return render_template('addbook.html')

"""
#READS DATA FROM ADD BOOK PAGE
@app.route('/BookStore/addbook', methods = ['GET', 'POST'])
def addbook():
    if request.method == 'POST' and 'inputBookID' in request.form:
            inputBookID = request.form['inputBookID']
            mycursor.execute('Select * FROM Books WHERE Book_ID = %s', (inputBookID,))
            book = mycursor.fetchone()
            if len(book) > 0:
                #flash('Book already exists.')
                msg = 'Book already exists.'
                return redirect('/BookStore/viewadminprofile')
            else:
                inputTitle = request.form['inputTitle']
                inputAuthor = request.form['inputAuthor']
                inputPrice = request.form['inputPrice']
                inputPublisher = request.form['inputPublisher']
                inputSubject = request.form['inputSubject']
                
                bookFormula = "INSERT INTO Books (Title, Publisher_ID, Price, Subject, Author, Book_ID) VALUES (%s, %s, %s, %s, %s, %s)"
                bookInfo = (inputTitle, inputPublisher, inputPrice, inputSubject, inputAuthor, inputBookID)
                mycursor.execute(bookFormula, bookInfo)
                mydb.commit()
    else:
        msg = 'Please enter book ID.'
    return redirect('/BookStore/viewmanagebooks')
"""

#READS DATA FROM ADD BOOK PAGE
@app.route('/BookStore/addbook/', methods = ['GET', 'POST'])
def addbook():
    if request.method == 'POST' and 'inputBookID' in request.form:
        inputBookID = request.form['inputBookID']
        inputTitle = request.form['inputTitle']
        inputAuthor = request.form['inputAuthor']
        inputPrice = request.form['inputPrice']
        inputPublisher = request.form['inputPublisher']
        inputSubject = request.form['inputSubject']
                
        bookFormula = "INSERT INTO Books (Title, Publisher_ID, Price, Subject, Author, Book_ID) VALUES (%s, %s, %s, %s, %s, %s)"
        bookInfo = (inputTitle, inputPublisher, inputPrice, inputSubject, inputAuthor, inputBookID)
        mycursor.execute(bookFormula, bookInfo)
        mydb.commit()
    else:
        msg = 'Please enter book ID.'
    return redirect('/BookStore/viewmanagebooks')


#ROUTES TO EDIT BOOK PAGE
@app.route('/BookStore/editbook/')
def vieweditbook():
    return render_template('editbook.html')

#READS DATA FROM EDIT BOOK PAGE
@app.route('/BookStore/editbook/', methods = ['GET', 'POST'])
def editbook():
    if request.method== 'POST' and 'inputBookID' in request.form:
        inputBookID = request.form['inputBookID']
        mycursor.execute('Select * FROM Books WHERE Book_ID = %s', (inputBookID))
        book = mycursor.fetchone()
        if len(book) == 0:
            msg = 'Book does not exist.'
            return redirect('/BookStore/adminprofile')
        else:
            inputTitle = request.form['inputTitle']
            inputAuthor = request.form['inputAuthor']
            inputPrice = request.form['inputPrice']
            inputPublisher = request.form['inputPublisher']
            inputSubject = request.form['inputSubject']
            
            editTitle = "INSERT INTO Books SET Title = %s WHERE Book_ID = %s"
            editPublisher = "UPDATE Books SET Publisher = %s WHERE Book_ID = %s"
            editAuthor = "UPDATE Books SET Author = %s WHERE Book_ID = %s"
            editPrice = "UPDATE Books SET Price = %s WHERE Book_ID = %s"
            editSubject = "UPDATE Books SET Subject = %s WHERE Book_ID = %s"

            bookFormula = "INSERT INTO Books (Title, Publisher_ID, Author, Book_ID, Price, Subject) VALUES (%s, %s, %s, %s, %s, %s)"
            bookInfo = (inputTitle, inputPublisher, inputAuthor, inputBookID, inputPrice, inputSubject)
            mycursor.execute(bookFormula, bookInfo)
            mydb.commit()
            
    else:
        msg = 'Invalid input.'
    return redirect('/BookStore/adminprofile')

#ROUTES TO DELETE BOOK PAGE
@app.route('/BookStore/deletebook')
def viewdeletebook():
    return render_template('deletebook.html')

#READS DATA FROM DELETE BOOK PAGE
@app.route('/BookStore/deletebook', methods = ['GET', 'POST'])
def deletebook():
    if request.method== 'POST' and 'inputBookID' in request.form:
        inputBookID = request.form['inputBookID']
        mycursor.execute('Select * FROM Books WHERE Book_ID = %s', (inputBookID))
        book = mycursor.fetchone()
        if len(book) == 0:
            msg = 'Book does not exist.'
            return redirect('/BookStore/adminprofile')
        else:
            deleteBook = "DELETE FROM Books WHERE Book_ID = %s"
            bookInfo = (inputBookID)
            mycursor.execute(deleteBook, bookInfo)
            mydb.commit()
            return redirect('/BookStore/adminprofile')
            
    else:
        msg = 'Please enter book ID.'
    return redirect('/BookStore/adminprofile')

#READS DATA FROM DELETE BOOK PAGE
@app.route('/BookStore/deletebook', methods = ['GET', 'POST'])
def managebooks():
    ####For edit books
    if request.method == 'POST' and 'inputSearchManage' in request.form:
        inputSearchManage = request.form['inputSearchManage']
        mycursor.execute('Select * FROM Books WHERE Book_ID = %s', (inputSearchManage,))
        book = mycursor.fetchone()
        if len(book) == 0:
            #flash('Book does not exist.')
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
                #flash('Book already exists.')
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



###### :) :) :) 
#### Coding a temp database for the shopping cart


"""
@app.route('/add', methods=['POST'])
def add_product_to_cart():
	try:
		_quantity = int(request.form['quantity'])
		_code = request.form['code']
		# validate the received values
		if _quantity and _code and request.method == 'POST':
			mycursor.execute("SELECT * FROM Books WHERE Book_ID =%s", _code)
			row = cursor.fetchone()
			
			itemArray = { row[4] : {'title' : row[0], 'ISBN' : row[6], 'quantity' : _quantity, 'price' : row[5], 'image' : row[1], 'total_price': _quantity * row[5]}}
		#	title = row[0]
		#	pubID = row[2]
		#	pubDate = row[3]
		#	bookID = row[4]
		#	price = row[5]
		#	priceAll = _quantity * price
			
			
			session.modified = True
			if 'cart_item' in session:
				if row[4] in session['cart_item']:
					for key, value in session['cart_item'].items():
						if row[4] == key:
							#session.modified = True
							#if session['cart_item'][key]['quantity'] is not None:
							#	session['cart_item'][key]['quantity'] = 0
							old_quantity = session['cart_item'][key]['quantity']
							total_quantity = old_quantity + _quantity
							session['cart_item'][key]['quantity'] = total_quantity
							session['cart_item'][key]['total_price'] = total_quantity * row[5]
				else:
					session['cart_item'] = array_merge(session['cart_item'], itemArray)
				for key, value in session['cart_item'].items():
					individual_quantity = int(session['cart_item'][key]['quantity'])
					individual_price = float(session['cart_item'][key]['total_price'])
					all_total_quantity = all_total_quantity + individual_quantity
					all_total_price = all_total_price + individual_price
			else:
				session['cart_item'] = itemArray
				all_total_quantity = all_total_quantity + _quantity
				all_total_price = all_total_price + _quantity * row['price']
			
			session['all_total_quantity'] = all_total_quantity
			session['all_total_price'] = all_total_price
			
			return redirect('/BookStore/cart')
		else:
			return 'Error while adding item to cart'
	except Exception as e:
		print(e)
"""



#@app.route('/add', methods=['POST'])
#def view_cart():
#	return render_template('cart.html')

@app.route('/BookStore/add<BookID>/')
def addToCart(BookID):
	return render_template('cart.html')


@app.route('/BookStore/add?bookid=/')
def addCart():
	return render_template('cart.html')


###variable for cart.


#ROUTES TO CART PAGE
### :) :) :) Cart updates dynamically based on bookID retrieved from search page addCart form
@app.route('/BookStore/cart/', methods=['POST'])
def addBookCart():
    bookID = request.form['bookid']
    quantity = request.form['quantity']
    print('Book ID is: ' + bookID)
    print('Quantity: ' + quantity)

    #get book
    mycursor.execute("SELECT Title, Author, Price, Subject, Book_ID FROM Books WHERE Book_ID = %s", (bookID,))
    book = mycursor.fetchall()
    print("Adding book to cart:", book[0])

    #insert into cart
    for x in range(int(quantity)):
        cartInsert = "INSERT INTO cart (Title, Author, Price, Subject, Book_ID) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(cartInsert, book[0])
        mydb.commit()

    #get books in cart
    mycursor.execute("SELECT Title, Author, Price, Subject, Book_ID FROM cart")
    bookData = mycursor.fetchall()

    #get price
    mycursor.execute("SELECT SUM(Price) FROM cart")
    price = mycursor.fetchall()
    price = str(price[0][0])

    if price == "None":
        return render_template('cart.html', data=bookData, price="--")
    else:
        return render_template('cart.html', data=bookData, price="{:.2f}".format(float(price)))

@app.route('/BookStore/remove/', methods=['POST'])
def remove():
    #remove book from cart
    bookID = request.form['bookid']

    if bookID == "x":
        mycursor.execute("DELETE FROM cart")
        mydb.commit()
        return redirect('/BookStore/cart/')
    else:
        quantity = request.form['quantity']
        if quantity == "all":
            mycursor.execute("DELETE FROM cart WHERE Book_ID = %s", (bookID,))
            mydb.commit()
        else:
            mycursor.execute("DELETE FROM cart WHERE Book_ID = %s LIMIT 1", (bookID,))
            mydb.commit()
        return redirect('/BookStore/cart/')

#ROUTES TO CART PAGE, GET Retrieval
# :) :) :) passes in cart data to cart.html template in order to display all items in cart
@app.route('/BookStore/cart/')
def viewCart():
    #get books in cart
    mycursor.execute("SELECT Title, Author, Price, Subject, Book_ID FROM cart")
    bookData = mycursor.fetchall()

    #get price
    mycursor.execute("SELECT SUM(Price) FROM cart")
    price = mycursor.fetchall()
    price = str(price[0][0])

    if price == "None":
        return render_template('cart.html', data=bookData, price="--")
    else:
        return render_template('cart.html', data=bookData, price="{:.2f}".format(float(price)))

#MAIN METHOD
if __name__=="__main__":
	app.run(port=8000, debug=True)
