from datetime import datetime
from . import db, UserModel

class RoomModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=True, default=None)
    owner_id = db.Column(db.Integer, db.ForeignKey("user_model.id"))
    messages = db.Column(db.String, unique=True, nullable=True)
