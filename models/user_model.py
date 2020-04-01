from . import db
from hashlib import sha256, md5
from datetime import datetime
import time

class UserModel(db.Model):

    """
    Defines the required user data to store in database.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    user_key = db.Column(db.String, unique=True, nullable=False)
    rooms = db.relationship("RoomModel", backref="owner")
    creation_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class UserModelHandler(object):

    """
    You should create the UserModel object through this handler.
    It validates the data and changes necessary things.
    """

    def __init__(self, username, email, password):
        self.username = username
        self.email = email

        self.hash_password(password)
        self.user_key = self.generate_user_key(username)

    # Convert raw password to more secure, hashed form
    def hash_password(self, password):
        hash = sha256(password.encode("utf-8")).hexdigest()
        self.password = hash

    # Set unique user_key for security reasons
    @staticmethod
    def generate_user_key(username):
        raw_unique_key = "".join([username, str(time.time())])
        user_key = md5(raw_unique_key.encode("utf-8")).hexdigest()
        return user_key

    # Finalize the model state
    def set(self):
        instance = UserModel(username=self.username, email=self.email, password=self.password, user_key=self.user_key)
        return instance

    @staticmethod
    def save(instance):
        db.session.add(instance)
        db.session.commit()
        return instance
