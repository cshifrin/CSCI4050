#solely testing my register code

import mysql.connector

userID = 21
addressID = userID
cardID = userID

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="password",
	database="BookStore"
)
mycursor=mydb.cursor()

regFormula = "INSERT INTO Users (User_ID, First_Name, Last_Name, Email, Cell_Phone, Password, Status, Recieve_Promotion, User_Type_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

regAddressFormula = "INSERT INTO Addresses (User_ID, Address_ID, Street, City, State, Country, Zip_Code) VALUES (%s, %s, %s, %s, %s, %s, %s)"

regCardFormula = "INSERT INTO Payment_Cards (User_ID, Address_ID, Card_ID, Card_Number, Type_ID, Expiration_Date, Holder_Name) VALUES (%s, %s, %s, %s, %s, %s, %s)"

n = True

if n:
	
	inputName = 'Bob Builder'
	inputPhone = '12345678900'
	inputEmail = 'bob@uga.edu'
	inputPassword = 'password'
	inputAddress = '123 address rd' 
	inputCity = 'Athens'
	inputState = 'Georgia'
	inputZip = '30605'	
	inputCountry = 'USA'
	inputCardNo = '0000'
	inputCardDate = '2021-11-12'
	inputCardName = 'Bob Builder'

	print(inputName + ' ' + inputPhone + ' ' + inputEmail)
	nameList = inputName.split()
	firstName = nameList[0]
	lastName = nameList[1]
	regInfo = (userID, firstName, lastName, inputEmail, inputPhone, inputPassword, 0, 0, 2)
	mycursor.execute(regFormula, regInfo)
	mydb.commit()

	addInfo = (userID, addressID, inputAddress, inputCity, inputState, inputCountry, inputZip)
	mycursor.execute(regAddressFormula, addInfo)
	
	mydb.commit()

	cardInfo = (userID, addressID, cardID, inputCardNo, 1, inputCardDate, inputCardName) 
	mycursor.execute(regCardFormula, cardInfo)
	
	mydb.commit()
	userID = userID+1
	addressID = addressID+1
	cardID = cardID +1


