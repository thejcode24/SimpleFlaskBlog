from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    """ 
    Class that represents a registration form which contains separate fields to 
    enter user information you would typically see in a user registration form online. 
    By importing various extensions within the WTForms extension of Flask,
    you can create text fields that take input and validate the information 
    according to the set validators in the validators field. 
    
    """
    
    username = StringField("Username", 
                            validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Password",
                            validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", 
                            validators=[DataRequired(), EqualTo('password')])
    email = StringField("Email",
                            validators=[DataRequired(), Email()])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    """ 
    Similar to RegistrationForm, but instead contains fields to check for login 
    using user's email and password.

    """
    email = StringField("Email",
                            validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                            validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")
