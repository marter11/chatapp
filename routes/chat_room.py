from flask import render_template
from . import app, RoomModel

@app.route("/room/<int:id>")
def char_room(id):
    return render_template("room_related/chat_room.html")
