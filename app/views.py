# Import flask dependencies
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for

# Define the blueprints
home = Blueprint('home', __name__)
dash = Blueprint('dash',__name__)

# route for landing pafe
@home.route('/', methods=['GET', 'POST'])
def landing_page():
    return render_template('index.html')

#route for signup
@home.route('/signup/', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


#route for sigin
@home.route('/signin/', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')

@dash.route('/dashboard/', methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')
