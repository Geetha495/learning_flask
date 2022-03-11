from operator import le
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, length


class SignupForm(Form):
        first_name = StringField('First name',validators=[DataRequired("Please enter First Name")])
        last_name = StringField('Last name',validators=[DataRequired("Please enter Last Name")])
        email = StringField('Email',validators=[DataRequired("Please enter Email"),Email("Enter a valid email adress")])
        password = PasswordField('Password',validators=[DataRequired("Please enter Password"),length(min=5,message="Password should contain atleast 5 characters")])
        submit = SubmitField('Sign up')


class LoginForm(Form):
        email = StringField('Email',validators=[DataRequired("Please enter Email"),Email("Enter a valid email adress")])
        password = PasswordField('Password',validators=[DataRequired("Please enter Password"),length(min=5,message="Password should contain atleast 5 characters")])
        submit = SubmitField('Login')

class AddressForm(Form):
        address = StringField('Address',validators=[DataRequired("Please enter an address")])
        search = SubmitField('Search')