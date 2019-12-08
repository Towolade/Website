from flask_wtf import Form
from wtforms import IntegerField, TextField, BooleanField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired

class signUpForm(Form):

    userName = TextField('Username', validators=[DataRequired()])
    firstName = TextField('First Name', validators=[DataRequired()])
    lastName = TextField('Last Name', validators=[DataRequired()])
    DOB = DateField('Date Of Birth', validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    eventOrganiser = BooleanField('Event Organiser')
    submit = SubmitField('Sign Up')

class loginForm(Form):

    userName = TextField('Username', validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Sign In')





