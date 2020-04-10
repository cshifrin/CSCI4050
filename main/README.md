CSCI 4050/6050  
Software Engineering 

Online Bookstore System 

Deliverable 6

Team 8
Team Members

- Mohammed Aldosari
- Daniel Garcia
- Angela Tsao
- Chris Shifrin

To open this project and you are using a Mac, go to this directory containing the .php files and type the following:

php -S localhost:8000

Then, go to your web browser and as enter localhost:8000 in the URL. If you are using anything other than a Mac, you need to download something like XAMPP or WAMP and follow that process accordingly. The home page is titled index.php.

The following files contain .php code that needs to be edited and connected to the database. Comments written in all caps are what need to be implemented.
- editprofile.php
- forgotpass.php
- reg.php
- regcon.php
- signin.php

To sign in to the website, the only current working accounts are the following two. They aren't in the database or anything, the 5 files above are just hardcoded to check for these existing accounts. For example, if you try to enter an email that doesn't 'exist' in the forgot password page, you will get an error.
- user@email.com, password
- admin@email.com, password

Also, the current hardcoded confirmation number to confirm your email is 123.
