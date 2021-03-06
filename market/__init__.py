from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# created an instance of the flask app
app = Flask(__name__)

# creating a file that will recoginze as our db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# configuration so as to display the Flask form
app.config['SECRET_KEY'] = 'd5fe45950371e31e517f7551'

# created an instance of the database
db = SQLAlchemy(app)

# creating an instance of the bcrypt --> to hash out password/
bcrypt = Bcrypt(app)

# creating an insatnce of the login manager--> to manager our login
login_manager = LoginManager(app)

# telling the login_manage the login_page route-- so it will direct the
# user to login page from home page if not logged in
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'

from market import routes
