# Import flask dependencies
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for
from app.user_management import UserRegister, FormSubmission
from app.mock_data import User, ShopList

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

        elif form_submit == "password_error":
            flash('passwords did not match', 'error')
            return render_template('signup.html')
        elif form_submit == "username_error" or form_submit == "email_error":
            flash('username or email already exists', 'error')
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
            slist = ShopList().list_name
            return redirect(url_for('dash.dashboard', slist=slist, username = User.user_name))
        if login_submit == "blank_entry":
            flash('Please fill all the fields before submit', 'error')
            return render_template('signin.html')

        if login_submit == "details_error":
            flash('incorrect password or username', 'error')
            return render_template('signin.html')
    return render_template('signin.html')

#this route links to the dashboard
@dash.route('/dashboard/', methods=['GET','POST'])
def dashboard():

    slist = ShopList().list_name
    return render_template('dashboard.html', username=User.user_name, slist=slist)

#adding new shopping lists
@dash.route('/dashboard/add-shoppinglist/', methods=['GET','POST'])
def add_shoppinglist():
    if request.method == "POST":
        listname = request.form['listname']
        form_submit = FormSubmission().after_add_list(listname)
        if form_submit == "success":
            #at this point all the details are verified and the list is added.
            flash('shopping list added successfully', 'success')
            slist = ShopList().list_name
            return redirect(url_for('dash.dashboard', username=User.user_name, slist=slist))
        elif form_submit == "blank_entry":
            flash('Please enter a name', 'error')
            return render_template('add_shoppinglist.html', username=User.user_name)
        elif form_submit == "duped_entry":
            flash('You already have a shopping list with this name', 'error')
            return render_template('add_shoppinglist.html', username=User.user_name)
        else:
            flash('nothing happened', 'error')
            return render_template('add_shoppinglist.html', username=User.user_name)

    return render_template('add_shoppinglist.html', username=User.user_name)

#shopping lists view
@dash.route('/dashboard/shoppinglist/', methods=['GET','POST'])
def shoppinglist():

    slist = ShopList().list_name
    return render_template('shoppinglist.html', username=User.user_name,slist=slist)

#adding new friends
@dash.route('/dashboard/add-friend/', methods=['GET','POST'])
def add_buddy():
    return render_template('addBuddy.html', username=User.user_name)

#adding new zones
@dash.route('/dashboard/add-zone/', methods=['GET','POST'])
def add_zone():
    return render_template('addzone.html', username=User.user_name)
