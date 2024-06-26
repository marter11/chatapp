from flask_socketio import SocketIO
from flask import Flask

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

# Settings
DEBUG = True

# Models
import models
from models import UserModelHandler, RoomModel

# Middlewares
from middlewares.authentication_middleware import AuthenticationMiddleware

# Views
from . import login, register, home, chat_room, room_menu, oauth
