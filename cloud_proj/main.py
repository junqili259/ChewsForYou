import os
import logging


from flask import Flask, render_template, url_for, redirect, request, Response, flash
from forms import AddressForm, RegisterForm, LoginForm, SupportForm
import requests, random
from api import business_search
import sqlalchemy


db_user = os.environ.get("CLOUD_SQL_USERNAME")
db_pass = os.environ.get("CLOUD_SQL_PASSWORD")
db_name = os.environ.get("CLOUD_SQL_DATABASE_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")



app = Flask(__name__)


logger = logging.getLogger()


db = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        username=db_user,
        password=db_pass,
        database=db_name,
        query={"unix_socket": "/cloudsql/{}".format(cloud_sql_connection_name)},
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,
    pool_recycle=1800,
)



#app.config['SECRET_KEY'] = '53ba0078b3c38695e0697cf2f4c8bd79'
app.config['SECRET KEY'] = os.environ.get("KEY")


#Home page where user can login or create an account
#def homePage():
@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html')


# For testing api functions only
# Will not be in final implementation
@app.route('/register', methods=['GET','POST'])
def register():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        
        #   The sql statement for the database
        stmt = sqlalchemy.text("INSERT INTO Account(fname,lname,email,user,password)" "VALUES(:fname,:lname,:email,:user,:password)")

        try:
            with db.connect() as conn:

                #   Executing the sql statement
                conn.execute(stmt,fname=first_name,lname=last_name,email=email,user=username,password=password)

        except Exception as e:
            logger.exception(e)

            # Username may have been taken already
            # Email cannot be used again for another registration
            # Flash the user an error message
            flash('Username already exists')
            return redirect(url_for('register'))
            #return Response(status=500,response="username already exists")


        #return Response(status=200,response="Success")
        return redirect(url_for('address'))
    
    return render_template('register.html',form=registerForm)
    


# Login page for users with a pre-existing account
@app.route("/login", methods=['GET','POST'])
def login():
    #Create and pass login form to login webpage
    loginForm = LoginForm()


    if loginForm.validate_on_submit():

        username = request.form.get('username')
        password = request.form.get('password')

        stmt = sqlalchemy.text("SELECT password FROM Account WHERE user=:user")

        try:
            with db.connect() as conn:
                result = conn.execute(stmt,user=username).fetchone()
                user_password = result[0]

                # if account exist redirect to address page
                if user_password == password:
                    return redirect(url_for('address'))


        except Exception as e:
            logger.exception(e)

            # if account doesn't exist flash error message
            flash('Invalid Username and Password')
            return redirect(url_for('login'))

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
    



@app.route("/support", methods=['GET','POST'])
def support():
    supportForm = SupportForm()
    
    """
    if supportForm.validate_on_submit():
        # get email information
        # get subject information
        # get description of issue information
        # send data to blob storage

    """
    return render_template('support.html', form=supportForm)
