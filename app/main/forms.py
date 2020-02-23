from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User, Checkout

class CheckoutForm(FlaskForm):
    phone = StringField('Enter your phone number',validators=[Required()])
    bags = StringField( 'enter number of bags',validators = [Required()])
    Checkout = SubmitField('Find Location', validators = [Required()])