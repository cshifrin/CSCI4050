from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/home/signin/')
def about():
    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)
