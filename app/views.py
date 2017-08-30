# Import flask dependencies
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for
from app.user_management import UserRegister, FormSubmission

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
        form_submit = FormSubmission().after_user_submit_register(username, email, password, confirm_pass)
        if form_submit == "success":
            #at this point all the user data has been verified and should be saved
            flash('signup success', 'success')
            return redirect(url_for('home.signin'))
        elif form_submit == "blank_entry":
            flash('Please fill all the fields before submit', 'error')
            return render_template('signup.html')

        elif form_submit == "password_error":
            flash('passwords did not match', 'error')
            return render_template('signup.html')
        elif form_submit == "username_error":
            flash('username already exists', 'error')
            return render_template('signup.html')
        elif form_submit == "email_error":
            flash('email already exists', 'error')
            return render_template('signup.html')
        else:
            flash('nothing happened', 'error')
            return render_template('signup.html')


    return render_template('signup.html')


#route for sigin
@home.route('/signin/', methods=['GET', 'POST'])
def signin():
    #form submit
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        login_submit = FormSubmission().after_login_submit(username,password)
        if login_submit == "success":
            #at this point all the user data has been verified and should loged in
            flash('login success', 'success')
            return redirect(url_for('dash.dashboard'))
        elif login_submit == "blank_entry":
            flash('Please fill all the fields before submit', 'error')
            return render_template('signin.html')

        elif login_submit == "details_error":
            flash('incorrect password or username', 'error')
            return render_template('signin.html')
        else:
            flash('nothing happened', 'error')
            return render_template('signin.html')
    return render_template('signin.html')

#this route links to the dashboard
@dash.route('/dashboard/', methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')
