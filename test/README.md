# TEST
this are the test used on the program.

## How to run.
  1. Ensure `nosetests` is installed. Note, if you installed requirements.txt, then you can safely skip this  step.
  2. navigate to the test folder and
  3. run `nosetests app_test.py`

## test 1
  this is a test for successful registration of a user. the test should receive success.
## test 2
  this is a test for unsuccessful registration of a user. the test should fail if it receives success.
## test 3
  this is a test for the two passwords given by user at registration. the test should receive password_error if the passwords dont match.
## test 4
  this is a test fto see if user alredy exists. the test should receive u_email_error if the user exists.

## test 5
  this is a test for successful login. the test should receive success.
## test 6
  this is a test for unsuccessful login. the test should fail if it receives success.
