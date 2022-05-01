from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# created an instance of the flask app
app = Flask(__name__)

# creating a file that will recoginze as our db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# configuration so as to display the Flask form
app.config['SECRET_KEY'] = 'd5fe45950371e31e517f7551'

# created an instance of the database
db = SQLAlchemy(app)

from market import routes
