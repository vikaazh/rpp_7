from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="memory://",
    default_limits=["200 per day", "50 per hour"],

)

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'fetch.login_post'


app = Flask(__name__)

app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:Пароль//postgres:@localhost:5432/база'
app.config['SQLAlchemy_TRACK_MODIFIVATTION'] = False
