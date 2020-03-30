from flask_sqlalchemy import SQLAlchemy
from routes import app, DEBUG

if DEBUG:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
    FILE_SYSTEM_PATH = "models/file_system/"
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = ""
    FILE_SYSTEM_PATH = ""

db = SQLAlchemy(app)

# Settings
SECRET_KEY = app.config["SECRET_KEY"]

# Models
from .user_model import UserModel, UserModelHandler
from .room_model import RoomModel
from .file_system import FileSystemHandler
