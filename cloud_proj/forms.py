from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length

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
    email = StringField('Email',validators=[DataRequired()])
    confirmEmail = StringField('Confirm Email', validators=[DataRequired()])
    username = StringField('Username',validators=[DataRequired()])
    password = StringField('Password',validators=[DataRequired()])
    confirmPassword = StringField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = StringField('Password',validators=[DataRequired()])
    submit = SubmitField('Submit')