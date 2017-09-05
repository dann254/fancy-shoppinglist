# Import flask dependencies
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for

from app import app, user_handler, list_handler, buddy_handler, zone_handler, item_handler

# Define the blueprints
home = Blueprint('home', __name__)
dash = Blueprint('dash',__name__)

def login_required():
    if "username" not in session:
        flash('pleasse login to continue', 'error')
        return "fail"
    else:
        return "pass"
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
            slist = list_handler.return_shopping_list()
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

    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        slist = list_handler.return_shopping_list()
        blist = buddy_handler.return_buddies()
        zlist = zone_handler.return_zones()
        users = user_handler.return_users()
        my_buddies=[]
        username= str(session['username'])
        default = ""
        for i in blist:
            if i.get(username, default):
                my_buddies.append(i.get(username, default))

        return render_template('dashboard.html', username=session['username'], slist=slist, blist=blist, zlist=zlist, my_buddies=my_buddies)

#adding new shopping lists
@dash.route('/dashboard/add-shoppinglist/', methods=['GET','POST'])
def add_shoppinglist():
#displaying the add shopping list form and handling submission
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        if request.method == "POST":
            listname = request.form['listname']
            form_submit = list_handler.create_new_shoppinglist(listname, session['username'])
            if form_submit == "success":
                #at this point all the details are verified and the list is added.
                flash('shopping list added successfully', 'success')
                slist = list_handler.return_shopping_list()
                return redirect(url_for('dash.dashboard', username=session['username'], slist=slist))
            elif form_submit == "blank_entry":
                flash('Please enter a name', 'error')
                return render_template('add_shoppinglist.html', username=session['username'])
            else:
                flash('nothing happened', 'error')
                return render_template('add_shoppinglist.html', username=session['username'])

        return render_template('add_shoppinglist.html', username=session['username'])

#shopping lists view
@dash.route('/dashboard/shoppinglist/<list_id>', methods=['GET','POST'])
def shoppinglist(list_id):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        slist = list_handler.return_shopping_list()
        if slist == []:
            flash('you have no lists', 'info')
            return redirect(url_for('dash.dashboard'))
        for i in slist:
            try:

                if int(i['id'])==int(list_id):

                    zlist = zone_handler.return_zones()

                    ilist = item_handler.return_items()
                    return render_template('shoppinglist.html', username=session['username'],slist=i, zlist=zlist, ilist=ilist)
            except Exception as e:
                flash(str(e), 'error')
        flash('shoppinglist not found', 'error')
        return redirect(url_for('dash.dashboard'))

#friends shopping lists view
@dash.route('/dashboard/buddyshoppinglist/<list_id>', methods=['GET','POST'])
def buddyshoppinglist(list_id):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        slist = list_handler.return_shopping_list()
        if slist == []:
            flash('you have no lists', 'info')
            return redirect(url_for('dash.dashboard'))
        for i in slist:
            try:

                if int(i['id'])==int(list_id):
                    ilist = item_handler.return_items()
                    return render_template('buddyshoppinglist.html', username=session['username'],slist=i, ilist=ilist)
            except Exception as e:
                flash("shoppinglist not found", 'error')
        flash('shoppinglist not found', 'error')
        return redirect(url_for('dash.dashboard'))

#sharering shopping lists
@dash.route('/dashboard/share-list/<list_id>', methods=['GET'])
def share_list(list_id):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        if int(list_id):
            share = list_handler.share_shoppinglist(list_id)
            if share == "success":
                flash('shoppinglist share status changed', 'success')
                return redirect(url_for('dash.dashboard'))
            else:
                flash('something went wrong ', 'error')
                return redirect(url_for('dash.dashboard'))


        else:
            flash('shoppinglist not found', 'error')
            return redirect(url_for('dash.dashboard'))


#updating shopping lists
@dash.route('/dashboard/update-view/<list_id>', methods=['GET'])
def update_view(list_id):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        return render_template('update_shoppinglist.html', list_id=list_id)

#updating shopping lists
@dash.route('/dashboard/update-list/<list_id>', methods=['GET','POST'])
def update_list(list_id):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        if int(list_id) and request.method == "POST":
            new_name=request.form['newname']
            rename = list_handler.update_shoppinglist(list_id, new_name)
            if rename == "success":
                flash('rename successful', 'success')
                return redirect(url_for('dash.shoppinglist', list_id=list_id))
            else:
                flash('something went wrong', 'error')
                return redirect(url_for('dash.shoppinglist', list_id=list_id))


        else:
            flash('shoppinglist not found', 'error')
            return redirect(url_for('dash.dashboard'))

#updating shopping zone
@dash.route('/dashboard/add-shoppingzone/<list_id>', methods=['GET','POST'])
def add_shoppingzone(list_id):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        if int(list_id) and request.method == "POST":
            szone=request.form['zone']
            rename = list_handler.update_zone(list_id, szone)
            if rename == "success":
                flash('zoned', 'success')
                return redirect(url_for('dash.shoppinglist', list_id=list_id))
            else:
                flash('something went wrong', 'error')
                return redirect(url_for('dash.shoppinglist', list_id=list_id))


        else:
            flash('shoppinglist not found', 'error')
            return redirect(url_for('dash.dashboard'))



#adding new friends
@dash.route('/dashboard/add-friend/', methods=['GET','POST'])
def add_buddy():
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        return render_template('addBuddy.html', username=session['username'])
#adding new friends
@dash.route('/dashboard/add-friend/<parent>', methods=['GET','POST'])
def add_buddy_save(parent):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        if parent and request.method == "POST":
            new_buddy=request.form['buddyname']
            users=user_handler.return_users()
            buds = buddy_handler.return_buddies()
            existance = False
            for i in users:
                if i['username']== new_buddy:
                    existance=True
            refriend = False
            #for s in buds:
            #    if s[parent]==new_buddy:
            #        refriend=True
            if refriend==True:
                flash('you are already buddies add new buddy', 'error')
                return redirect(url_for('dash.add_buddy'))

            if new_buddy == parent:
                flash('you cant add yourself as a friend', 'error')
                return redirect(url_for('dash.add_buddy'))

            elif existance== True:
                befriend = buddy_handler.add_new_buddy(parent, new_buddy)
                if befriend == "success":
                    flash('buddy successfully invited', 'success')
                    return redirect(url_for('dash.dashboard'))
                else:
                    flash('something went wrong', 'error')
                    return redirect(url_for('dash.add_buddy'))

            else:
                flash('buddy does not have an account', 'error')
                return redirect(url_for('dash.add_buddy'))

        return redirect(url_for('dash.add_buddy'))

#adding new zones
@dash.route('/dashboard/add-zone/', methods=['GET','POST'])
def add_zone():
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        return render_template('addzone.html', username=session['username'])

@dash.route('/dashboard/add-zone/<username>', methods=['GET','POST'])
def add_zone_view(username):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        if username and request.method == "POST":
            new_zone=request.form['zone']
            szone = zone_handler.create_new_zone(username, new_zone)
            if szone == "success":
                flash('zone successfully added', 'success')
                return redirect(url_for('dash.dashboard'))
            else:
                flash('something went wrong', 'error')
                return redirect(url_for('dash.add_zone'))

        return redirect(url_for('dash.add_zone'))
# add item to shoppinglist
@dash.route('/dashboard/add-item/<list_id>', methods=['GET','POST'])
def add_item(list_id):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        if int(list_id) and request.method == "POST":
            item_string = request.form['item']
            item_list = item_string.split(',')
            if len(item_list)<3 or len(item_list)>3 :
                flash('please enter the specified details', 'warning')
                return redirect(url_for('dash.shoppinglist', list_id=list_id))
            try:
                int(item_list[1])
            except ValueError:
                flash('please enter item details in correct order and values', 'warning')
                return redirect(url_for('dash.shoppinglist', list_id=list_id))

            try:
                int(item_list[2])
            except ValueError:
                flash('please enter item details in correct order and values', 'warning')
                return redirect(url_for('dash.shoppinglist', list_id=list_id))

            form_submit = item_handler.create_new_item(item_list[0],item_list[1],item_list[2], list_id)
            if form_submit == "success":
                #at this point all the details are verified and the item is added.
                flash('item list added', 'success')
                ilist = item_handler.return_items()
                return redirect(url_for('dash.shoppinglist', list_id=list_id))
            elif form_submit == "blank_entry":
                flash('Please enter values', 'error')
                return redirect(url_for('dash.shoppinglist', list_id=list_id))
        else:
            flash('nothing happened', 'error')
            return redirect(url_for('dash.shoppinglist', list_id=list_id))

    return redirect(url_for('dash.shoppinglist', list_id=list_id))


#delete shoppinglist
@dash.route('/dashboard/delete-list/<list_id>')
def delete_list(list_id):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        if int(list_id):
            delete = list_handler.delete_list(list_id)
            if delete == "success":
                flash('shoppinglist deleted!', 'info')
                return redirect(url_for('dash.dashboard'))
            else:
                flash('something went wrong ', 'error')
                return redirect(url_for('dash.dashboard'))


        else:
            flash('shoppinglist not found', 'error')
            return redirect(url_for('dash.dashboard'))

#unfriend buddies
@dash.route('/dashboard/unfriend/<buddy>')
def delete_buddy(buddy):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        if str(buddy):
            delete = buddy_handler.delete_buddy(session['username'],buddy)
            if delete == "success":
                flash('buddy unfriended !', 'info')
                return redirect(url_for('dash.dashboard'))
            else:
                flash('something went wrong ', 'error')
                return redirect(url_for('dash.dashboard'))


        else:
            flash('buddy not found', 'error')
            return redirect(url_for('dash.dashboard'))

#delete zone
@dash.route('/dashboard/delete-zone/<zone>')
def delete_zone(zone):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        if str(zone):
            delete = zone_handler.delete_zone(session['username'],zone)
            if delete == "success":
                flash('zone deleted!', 'info')
                return redirect(url_for('dash.dashboard'))
            else:
                flash('something went wrong ', 'error')
                return redirect(url_for('dash.dashboard'))


        else:
            flash('zone not found', 'error')
            return redirect(url_for('dash.dashboard'))

#delete item
@dash.route('/dashboard/delete-item/<list_id>/<item_id>/')
def delete_item(list_id, item_id):
    if login_required()=="fail":
        return redirect(url_for('home.signin'))
    else:
        if int(item_id) and int(list_id):
            delete = item_handler.delete_item(item_id)
            if delete == "success":
                flash('item deleted!', 'info')
                return redirect(url_for('dash.shoppinglist', list_id=list_id))
            else:
                flash('something went wrong ', 'error')
                return redirect(url_for('dash.shoppinglist', list_id=list_id))


        else:
            flash('item not found', 'error')
            return redirect(url_for('dash.shoppinglist', list_id=list_id))

@app.route('/logout/')
def logout():
   # remove thesession if it is there
   session.pop('username', None)
   flash('successfully logged out', 'success')
   return redirect(url_for('home.landing_page'))
