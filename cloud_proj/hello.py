from flask import Flask, render_template, url_for, redirect, request
from forms import AddressForm
import requests
from api import business_search


app = Flask(__name__)

app.config['SECRET_KEY'] = '53ba0078b3c38695e0697cf2f4c8bd79'

# Testing api endpoints
@app.route("/apitest")
def hello_world():
    data = business_search()
    return data
    

#Home Page with an address form
@app.route('/', methods=['GET','POST'])
def submitAddress():
    addressForm = AddressForm()
    if addressForm.validate_on_submit():
        address = request.form.get('address')
        #city = request.form.get('city')
        #state = request.form.get('state')
        #zipcode = request.form.get('zipcode')
        #print(address, city, state, zipcode)
        #print(city)
        return redirect(url_for('newpage'))
    return render_template('home.html', form=addressForm)
    

@app.route("/newpage")
def newpage():
    return render_template('newpage.html')
