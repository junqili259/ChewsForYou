from flask import Flask, render_template, url_for, redirect, request
from forms import AddressForm, RegisterForm
import requests, random
from api import business_search


app = Flask(__name__)

app.config['SECRET_KEY'] = '53ba0078b3c38695e0697cf2f4c8bd79'

# For testing api functions only
# Will not be in final implementation
@app.route("/apitest")
def hello_world():
    address = ''
    data = business_search(address) 
    randomRestaurant = random.choice(data)
    return redirect(randomRestaurant)


# Address Form page where user enters address information to obtain a random eatery in response
@app.route('/', methods=['GET','POST'])
def submitAddress():
    
    # Create an address form object
    addressForm = AddressForm()
    
    # If user clicks submit button
    if addressForm.validate_on_submit():
        fullAddress = ''
        
        # Store user inputs to their corresponding variables
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        zipcode = request.form.get('zipcode')
        
        # Create full address string
        fullAddress = address + ", " + city + "," + state + " " + zipcode
        
        # Pass the full address to an api function call and receive data back
        data = business_search(fullAddress) 
        
        # Return a random restaurant url from the data
        randomRestaurant = random.choice(data)
        
        # redirect user to that url
        return redirect(randomRestaurant)
    return render_template('home.html', form=addressForm)
    

# Login page for users with a pre-existing account
@app.route("/login")
def login():
    return render_template('login.html')


# Signing up for a new account
@app.route("/register", methods=['GET','POST'])
def register():

    # Create a register form object
    registerForm = RegisterForm()
    return render_template('register.html', form=registerForm)