from . import db, SECRET_KEY
from hashlib import sha256, md5
import datetime
import time

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(), unique=False, nullable=False)
    user_key = db.Column(db.String(), unique=True, nullable=False)
    creation_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

class UserModelHandler(object):

    """
    You should create the UserModel object through this handler.
    It validates the data and changes necessary things.
    """

    def __init__(self, username, email, password):
        self.username = username
        self.email = email

        self.hash_password(password)
        self.set_user_key(username)


    # Convert raw password to more secure, hashed form
    def hash_password(self, password):
        hash = sha256(password.encode("utf-8")).hexdigest()
        self.password = hash

    # Set unique user_key for security reasons
    def set_user_key(self, username):
        raw_unique_key = username+str(time.time())[:5]
        user_key = md5(raw_unique_key.encode("utf-8")).hexdigest()
        self.user_key = user_key

    # Finalize the model state
    def set(self):
        instance = UserModel(username=self.username, email=self.email, password=self.password, user_key=self.user_key)
        return instance

    @staticmethod
    def save(instance):
        db.session.add(instance)
        db.session.commit()
