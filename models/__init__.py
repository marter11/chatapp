from routes import app, DEBUG
from flask_sqlalchemy import SQLAlchemy

if DEBUG:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = ""

db = SQLAlchemy(app)

# Settings
SECRET_KEY = app.config["SECRET_KEY"]

# Models
from .user_model import UserModel, UserModelHandler
from .room_model import RoomModel
