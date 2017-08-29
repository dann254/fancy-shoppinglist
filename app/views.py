# Import flask dependencies
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for
from app.user_management import UserRegister

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
    #form submit
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_pass = request.form['cpassword']
        #verify password similarity
        if UserRegister().verify_password_similarity(password, confirm_pass) == True:
            flash('signup success', 'success')
            return redirect(url_for('home.signin'))
        else:
            flash('passwords did not match', 'success')
            return render_template('signup.html')


    return render_template('signup.html')


#route for sigin
@home.route('/signin/', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')

#this route links to the dashboard
@dash.route('/dashboard/', methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')
