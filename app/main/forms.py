from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class CheckoutForm(FlaskForm):
    phone = StringField('Enter your phone number',validators=[Required(),phone()])
    bags = StringField( 'enter number of bags',validators = [Required()])
    