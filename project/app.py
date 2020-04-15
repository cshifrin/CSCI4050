from flask import Flask, render_template
app = Flask(__name__)

@app.route('/BookStore/')
def home():
    return render_template('home.html')

@app.route('/BookStore/signin/')
def signin():
    return render_template('signin.html')

@app.route('/BookStore/forgotpwd/')
def forgotpwd():
    return render_template('forgotpwd.html')

if __name__ == '__main__':
    app.run(debug=True)
