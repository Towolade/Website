from flask import Flask
from flask import render_template
from flask_login import LoginManager

app = Flask(__name__)


@app.route('/')
#@login_required
def homePage():
    return render_template('home.html')

# todo Finish Login Method
@app.route('/login')
def login():
    return render_template('login.html')

# todo Finish Register method
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()
