# Import flask and template operators
from flask import Flask, render_template


# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

#import blueprints
from app.views import home as home
from app.views import dash as dash

#register blueprints
app.register_blueprint(home)
app.register_blueprint(dash)
