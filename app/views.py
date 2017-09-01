# Import flask dependencies
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for

from app import app, user_handler, form_handler
from app.mock_data import User, ShopList

# Define the blueprints
home = Blueprint('home', __name__)
dash = Blueprint('dash',__name__)

# route for landing page
@home.route('/', methods=['GET', 'POST'])
def landing_page():
    return render_template('index.html')

#route for signup
@home.route('/signup/', methods=['GET', 'POST'])
def signup():
    # at form submit, this statement is excecuted
    if request.method == "POST":
        #request all the variables from the form.
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_pass = request.form['cpassword']
        form_submit = user_handler.register_new_user(username, email, password, confirm_pass)
        if form_submit == "success":
            #at this point all the user data has been verified and has been saved
            flash('signup success', 'success')
            return redirect(url_for('home.signin'))
        #if passwords dont match, an error message is sent to the user. the same happens if username and email already exist.
        elif form_submit == "password_error":
            flash('passwords did not match', 'error')
            return render_template('signup.html')
        elif form_submit == "u_email_error":
            flash('username or email already exists', 'error')
            return render_template('signup.html')


    return render_template('signup.html')


#route for sigin
@home.route('/signin/', methods=['GET', 'POST'])
def signin():
    # at form submit, this statement is excecuted
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        login_submit = user_handler.login(username,password)
        if login_submit == "success":
            #at this point all the user data has been verified and should loged in
            session['username']=username
            flash('login success', 'success')
            slist = ShopList().list_name
            return redirect(url_for('dash.dashboard', slist=slist, username =session['username']))
        #the system should reject blank entries
        if login_submit == "blank_entry":
            flash('Please fill all the fields before submit', 'error')
            return render_template('signin.html')
        #the system should reject and notify the user when their login is not authenticated.
        if login_submit == "details_error":
            flash('incorrect password or username', 'error')
            return render_template('signin.html')
    return render_template('signin.html')

#this route links to the dashboard
@dash.route('/dashboard/', methods=['GET','POST'])
def dashboard():
#this displays the dashboard to the user after login. It should be restricted to loggedin users only.

    if "username" not in session:
        flash('pleasse login to continue', 'error')
        return redirect(url_for('home.signin'))
    else:
        slist = ShopList().list_name
        return render_template('dashboard.html', username=session['username'], slist=slist)

#adding new shopping lists
@dash.route('/dashboard/add-shoppinglist/', methods=['GET','POST'])
def add_shoppinglist():
#displaying the add shopping list form and hanling submission
    if "username" not in session:
        flash('pleasse login to continue', 'error')
        return redirect(url_for('home.signin'))
    else:
        if request.method == "POST":
            listname = request.form['listname']
            form_submit = form_handler.after_add_list(listname)
            if form_submit == "success":
                #at this point all the details are verified and the list is added.
                flash('shopping list added successfully', 'success')
                slist = ShopList().list_name
                return redirect(url_for('dash.dashboard', username=session['username'], slist=slist))
            elif form_submit == "blank_entry":
                flash('Please enter a name', 'error')
                return render_template('add_shoppinglist.html', username=session['username'])
            elif form_submit == "duped_entry":
                flash('You already have a shopping list with this name', 'error')
                return render_template('add_shoppinglist.html', username=session['username'])
            else:
                flash('nothing happened', 'error')
                return render_template('add_shoppinglist.html', username=session['username'])

        return render_template('add_shoppinglist.html', username=session['username'])

#shopping lists view
@dash.route('/dashboard/shoppinglist/', methods=['GET','POST'])
def shoppinglist():
    if "username" not in session:
        flash('pleasse login to continue', 'error')
        return redirect(url_for('home.signin'))
    else:
        slist = ShopList().list_name
        return render_template('shoppinglist.html', username=session['username'],slist=slist)

#adding new friends
@dash.route('/dashboard/add-friend/', methods=['GET','POST'])
def add_buddy():
    if "username" not in session:
        flash('pleasse login to continue', 'error')
        return redirect(url_for('home.signin'))
    else:
        return render_template('addBuddy.html', username=session['username'])

#adding new zones
@dash.route('/dashboard/add-zone/', methods=['GET','POST'])
def add_zone():
    if "username" not in session:
        flash('pleasse login to continue', 'error')
        return redirect(url_for('home.signin'))
    else:
        return render_template('addzone.html', username=session['username'])

@app.route('/logout/')
def logout():
   # remove thesession if it is there
   session.pop('username', None)
   flash('successfully logged out', 'success')
   return redirect(url_for('home.landing_page'))
