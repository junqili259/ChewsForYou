import os
import logging
from flask import Flask, render_template, url_for, redirect, request, Response, flash
from forms import AddressForm, RegisterForm, LoginForm, SupportForm
import requests, random
from api import business_search
from firebase_admin import credentials, auth, firestore, initialize_app


app = Flask(__name__)
app.config.from_object('config.Config')

logger = logging.getLogger()

cred = credentials.Certificate('chewsforyou.json')
firebase_app = initialize_app(cred)
db = firestore.client()


#Home page where user can login or create an account
#def homePage():
@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html')


@app.route('/register', methods=['GET','POST'])
def register():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():

        #   Receive user input from register form
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            auth.create_user(display_name=username,email=email,password=password)

        except Exception as e:
            logger.exception(e)
            flash('Username already exists')
            return redirect(url_for('register'))

        return redirect(url_for('address'))
    
    return render_template('register.html',form=registerForm)
    


# Login page for users with a pre-existing account
@app.route("/login", methods=['GET','POST'])
def login():
    #Create and pass login form to login webpage
    loginForm = LoginForm()

    if loginForm.validate_on_submit():
        # Receive user input from login form
        username = request.form.get('username')
        password = request.form.get('password')


        """
        try:
            #   Execute sql statement
            with db.connect() as conn:
                result = conn.execute(stmt,user=username).fetchone()
                user_password = result[0]

                # if account exist redirect to address page
                if user_password == password:
                    return redirect(url_for('address'))
                else:
                    # flash message if username exist but password doesn't match
                    flash('Invalid Password')
                    return redirect(url_for('login'))
        

        except Exception as e:
            logger.exception(e)

            # if account doesn't exist flash error message
            flash('Invalid Username and Password')
            return redirect(url_for('login'))
        """

    return render_template('login.html', form=loginForm)



# Address Form page where user enters address information to obtain a random eatery in response
@app.route('/address', methods=['GET','POST'])
def address():
    
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
    return render_template('address.html', form=addressForm)
