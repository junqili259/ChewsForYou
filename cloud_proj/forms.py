from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email

#  Form for the user to input address details
class AddressForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = StringField('Zip Code', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Form for the user to input register details
class RegisterForm(FlaskForm):
    firstName = StringField('First Name',validators=[DataRequired()])
    lastName = StringField('Last Name',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(), Email()])
    confirmEmail = StringField('Confirm Email', validators=[DataRequired(), Email(), EqualTo('email')])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')