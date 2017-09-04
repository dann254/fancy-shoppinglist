import os
# Import flask and template operators
from flask import Flask, render_template
from app import user_management, list_management


# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
# initialize class
user_handler = user_management.UserManager()
list_hanler = list_management.ListManager()

#import blueprints
from app.views import home as home
from app.views import dash as dash

#register blueprints
app.register_blueprint(home)
app.register_blueprint(dash)
