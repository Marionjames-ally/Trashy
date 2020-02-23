
from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import User,Checkout
from .. import db 
from .forms import CheckoutForm
from ..request import getLocation

@main.route('/',methods = ["GET", "POST"])
@main.route('/index', methods = ["GET", "POST"])
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
    checkout_form = CheckoutForm()
    if checkout_form.validate_on_submit():    
        phone = checkout_form.phone.data
        bags = checkout_form.bags.data
        location = getLocation()
        latitude = location[0]
        longitude = location[1]
        new_checkout = Checkout(phone=phone,bags=bags,latitude=latitude,longitude=longitude)
        new_checkout.save_checkout()
        
        return redirect('map') 
    flash('checkout complete check your email for more details', 'success')   
    return render_template("request_form.html", checkout_form = checkout_form)

@main.route('/map', methods = ["GET","POST"])
def map():
    location = getLocation()
    latitude = location[0]
    longitude =location[1]

    return render_template('maps.html', latitude=latitude, longitude = longitude)