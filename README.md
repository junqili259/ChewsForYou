# ChewsForYou

## Steps for setting up this project

1. Install the latest version of [python 3.0+](https://www.python.org/downloads/)

2. Clone this repository

3. Through command-line, navigate into the cloud_proj directory of this project from where you stored it. Create a virtual environment with the following commands.

**Note:** If you don't have the virtualenv package already then perform the following command to install it before proceeding.
```
$ pip install virtualenv
```

```
$ virtualenv env
$ source env/bin/activate
```

4. Now that you created your virtual environment and activated it, we want to install the neccessary packages.

```
$ pip install flask
$ pip install requests
$ pip install flask-wtf
```

## Running the live server on your pc

The virtual environment has to be running. After it's activated enter the following:

For Mac/Linux/WSL users:
```
$ export FLASK_APP=hello.py
$ flask run
```

For Windows users:
```
$ set FLASK_APP=hello.py
$ flask run
```
