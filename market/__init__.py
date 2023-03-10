from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# tell flask where the database can be found
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
# initialize db with SQLAlchemy class
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# Tell flask where is the login page, it is used by login_required decorator in routes.py
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
from market import routes
