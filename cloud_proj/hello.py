from flask import Flask, render_template, url_for, redirect
from forms import AddressForm
import requests


app = Flask(__name__)

app.config['SECRET_KEY'] = '53ba0078b3c38695e0697cf2f4c8bd79'

@app.route("/apitest")
def hello_world():
    #return render_template('home.html')
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London&appid=93a0a96f6526590b3123ee6d5ea16fa9')
    r_dict = r.json()
    return r_dict['main']


#Home Page with an address form
@app.route('/', methods=['GET','POST'])
def submitAddress():
    addressForm = AddressForm()
    if addressForm.validate_on_submit():
        return redirect(url_for('newpage'))
    return render_template('home.html', form=addressForm)
    

@app.route("/newpage")
def newpage():
    return render_template('newpage.html')
