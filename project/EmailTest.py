##set status from 0 (inactive) to 1 (active)

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

#set status from 0 (inactive) to 1 (active)
newStatus = ("1", userID)
statusFormula = "UPDATE Users SET Status = %s WHERE User_ID = %s"

###########
if confirmation == code: 
    mycursor.execute(statusFormula, newStatus)

mydb.commit()
