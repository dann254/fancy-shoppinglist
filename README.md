[![Codacy Badge](https://api.codacy.com/project/badge/Grade/644d536ad2664d2a96934040e4a2d240)](https://www.codacy.com/app/dann254/fancy-shoppinglist?utm_source=github.com&utm_medium=referral&utm_content=dann254/fancy-shoppinglist&utm_campaign=badger)
[![Build Status](https://travis-ci.org/dann254/fancy-shoppinglist.svg?branch=flask-basics)](https://travis-ci.org/dann254/fancy-shoppinglist)
[![Code Climate](https://codeclimate.com/github/dann254/fancy-shoppinglist/badges/gpa.svg)](https://codeclimate.com/github/dann254/fancy-shoppinglist/)
[![Coverage Status](https://coveralls.io/repos/github/dann254/fancy-shoppinglist/badge.svg)](https://coveralls.io/github/dann254/fancy-shoppinglist)

# FANCY_SHOPPINGLIST
This is an innovative shopping list app that allows users to record and share things they want to spend money on. The app keeps track of their shopping lists.

# installation procedure.
  1. Ensure you have *python 3*, *virtualenv* and *pip* installed on your local machine.
  2. Clone the project locally.
  3. navigate to the project folder.
  4. create a virtual environment. example `mkvirtualenv fancy`
  5. work on the virtual environment you just created. `workon fancy`
  6. install the requirements in the environment. `pip install -r requirements.txt`

# Running the app
  1. `python runserver.py`

  **Note**: *cdn version of bootsrap is used in this app. make sure you have internet connection when running the app*

# Deployed on heroku
  https://salty-stream-46784.herokuapp.com/

# running tests.
  instructions for running tests are available within the test folder.

  **note** travis-ci is set to run the test automatically on this repository

# folder structure.
```
~/fancy-shoppinglist
  |-- runserver.py
  |-- config.py
  |-- requirements.txt
  |-- README.md
  |-- Procfile
  |-- .travis.yml
  |-- .gitignore
  |__ /app      
       |-- __init__.py
       |-- views.py
       |-- user_management.py
       |-- buddy_management.py
       |-- item_management.py
       |-- list_management.py
       |-- zone_managent.py
       |__ /templates
            |-- *all templates used by flask most of the extend base templates to save memory and make them more mentainable*
       |__ /static
            |-- *all images and css files*
  |__ /designs
        |-- *HTML/CSS designs and UML diagrams*
  |__ /tests
        |-- __init__.py
        |-- app_test.py
        |-- README.md
  |__ /wireframes
        |-- *all wireframe designs for the UI*
```
## The following are folders that contain the html/css designs, UML class diagram and wireframes for the app

## designs
  1. This folder contains all the html designs and the UML class diagram.
  2. More details are found in the README.md within the folder.

## wireframes
  1. This folder contains the wireframes for the app.
  2. More details are found in the README.md within the folder.
