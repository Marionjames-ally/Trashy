
from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import User
from .. import db 
from .forms import CheckoutForm

@main.route('/', methods = ["GET", "POST"])
def index():
    '''
    root page that returns the home page and its data
    '''
    return render_template('index.html')

@main.route('/checkout', methods =["GET", "POST"])
def checkout():
    '''
    function that returns the checkout
    '''
    form = CheckoutForm()
    if form.validate_on_submit():
        