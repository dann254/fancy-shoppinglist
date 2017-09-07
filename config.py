# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for signing the data.
CSRF_SESSION_KEY = "elevat3dSeaM0nster"

# Secret key for signing cookies
SECRET_KEY = "elevat3dSeaM0nster"

PORT=5000
