from flask import Flask
from .forms import signUpForm, loginForm
from app import app
from flask import render_template
from flask_login import LoginManager


@app.route('/')
# @login_required
def homePage():
    return render_template('home.html')

# todo Finish Login Method
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    return render_template('login.html', form = form)

# todo Finish Register method
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = signUpForm()
    return render_template('register.html')

@app.route('/create%events', methods=['GET', 'POST'])
def createEvents():
    return render_template('createEvents.html')

@app.route('/profile')
def userProfile():
    return render_template('userInfo.html')

@app.route('/get%tickets')
def getTickets():
    return render_template('tickets.html')


