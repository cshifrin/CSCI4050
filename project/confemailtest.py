from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/BookStore/signin/') #,methods =['GET', 'POST'])
def about():
    inputEmail = 'alt07134@uga.edu'
    if request.method=='GET':
#    	return render_template('signin.html')
#   if request.method=='POST':
        confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

        confirm_url = url_for('users.confirm_email', 
        token=confirm_serializer.dumps(inputEmail, salt='email-confirmation-salt'), _external=True)

        html = render_template('emailContent.html', confirm_url=confirm_url)

        send_email('Confirm Your Email Address', [inputEmail], html)
        flash('Thanks for registering! Please confirm your account by finding the message sent to your email address.', 'success')
        return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)
