from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, SubmitField
from wtforms.validators import email, length, DataRequired

class SignupForm(FlaskForm):
    email=StringField("Please enter your email", validators=[DataRequired("Your input cannot be null"),
                                                             email("This did not look like an email")])

    first_name=StringField("PLease enter your first name", validators=[DataRequired("Your input cannot be null")])

    last_name = StringField("Please enter your last name",validators=[DataRequired("Your input cannot be null")])
    password=PasswordField("Password: ", validators=[DataRequired("Your input cannot be null"), length(min=5, message="PW must be more than 5 characters")])
    submit = SubmitField("Submit")