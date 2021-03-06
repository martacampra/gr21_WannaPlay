from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


from flaskblog.users.routes import users
from flaskblog.events.routes import events
from flaskblog.main.routes import main
from flaskblog.errors.handlers import errors
app.register_blueprint(users)
app.register_blueprint(events)
app.register_blueprint(main)
app.register_blueprint(errors)

