##Edit profile


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


###UNIT TESTS MANUAL INPUT###
newFirstName = ("Happy", userID)
newLastName = ("Hal" , userID)
email = ("happy@gmail.com", userID)
cell = ("1234567890", userID)
newPass = ("password", userID)

addr = ("13 sunshine st", userID)
city = ("Athens", userID)
state = ("GA", userID)
country = ("USA", userID)
zip = ("30605", userID)

num = ("111122223333", userID)
exp = ("2020-02-12", userID)
name = ("Happy Hal", userID)




#editFormula = "UPDATE Users SET (First_Name, Last_Name, Email, Cell_Phone, Password) WHERE 

editNameFormula = "UPDATE Users SET First_Name = %s WHERE User_ID = %s"
editLNameFormula = "UPDATE Users SET Last_Name = %s WHERE User_ID = %s"
editEmailFormula = "UPDATE Users SET Email = %s WHERE User_ID = %s"
editPhoneFormula = "UPDATE Users SET Cell_Phone = %s WHERE User_ID = %s"
editPassFormula = "UPDATE Users SET Password = %s WHERE User_ID = %s"

changes = (newFirstName, newLastName, email, cell, newPass)

mycursor.execute(editNameFormula, newFirstName)
mycursor.execute(editLNameFormula, newLastName)
mycursor.execute(editEmailFormula, email)
mycursor.execute(editPhoneFormula, cell)
mycursor.execute(editPassFormula, newPass)

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

##########


editNumFormula = "UPDATE Payment_Cards SET Card_Number = %s WHERE User_ID = %s"
editExpFormula = "UPDATE Payment_Cards SET Expiration_Date = %s WHERE User_ID = %s"
editNameFormula = "UPDATE Payment_Cards SET Holder_Name = %s WHERE User_ID = %s"

mycursor.execute(editNumFormula, num)
mycursor.execute(editExpFormula, exp)
mycursor.execute(editNameFormula, name)

mydb.commit()