from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'danielgarcia'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Lizbeth77!'
app.config['MYSQL_DATABASE_DB'] = 'BookStore'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route('/BookStore/search/', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        book = request.form['inputSearch']
        # search by author or book
        cursor.execute("SELECT title, author, subject, Book_ID from Books WHERE title LIKE %s OR author LIKE %s OR subject LIKE %s", (book, book, book))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and book == 'all': 
            cursor.execute("SELECT title, author, subject, Book_ID from Books")
            conn.commit()
            data = cursor.fetchall()
        return render_template('search.html', data=data)
    return render_template('search.html')

@app.route('/BookStore/unregsearch/', methods=['GET', 'POST'])
def unregsearch():
    if request.method == "POST":
        book = request.form['inputSearch']
        # search by author or book
        cursor.execute("SELECT title, author, subject, Book_ID from Books WHERE title LIKE %s OR author LIKE %s OR subject LIKE %s", (book, book, book))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and book == 'all': 
            cursor.execute("SELECT title, author, subject, Book_ID from Books")
            conn.commit()
            data = cursor.fetchall()
        return render_template('unregsearch.html', data=data)
    return render_template('unregsearch.html')

if __name__ == '__main__':
    app.debug = True
    app.run()