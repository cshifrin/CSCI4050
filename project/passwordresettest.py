##change password

import smtplib, ssl
import random
import mysql.connector

port = 465  # For SSL
password = "@Bookstoreuga4050"

userID = 20

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
currentpwd = "password"

current = input("To change password, enter current password: ")

if current == currentpwd:


# Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login("bookstoreuga4050@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="BookStore"
    )
    mycursor=mydb.cursor()

    confirmation = input("What's the code? ")
    newPassword = input("What's your new password? ")
    newConf = input("Please confirm your new password, type it again: ")


    #change password
    newPass = (newConf, userID)
    passFormula = "UPDATE Users SET Password = %s WHERE User_ID = %s"

    ###########
    if confirmation == code: 
        if newPassword == newConf: 
            mycursor.execute(passFormula, newPass)
            mydb.commit()
