from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  


USER = {
    'username': 'admin',
    'password': 'password123'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER['username'] and password == USER['password']:
            otp = random.randint(100000, 999999)
            session['otp'] = str(otp)
            print(f"Generated OTP (for demo): {otp}")  
            return redirect(url_for('otp'))
        else:
            return "Invalid username or password"
    return render_template('login.html')

@app.route('/otp', methods=['GET', 'POST'])
def otp():
    if request.method == 'POST':
        user_otp = request.form['otp']
        if user_otp == session.get('otp'):
            return "Login successful!"
        else:
            return "Invalid OTP"
    return render_template('otp.html')

if __name__ == '__main__':
    app.run(debug=True)
