from . import app, RoomModel, socketio, AuthenticationMiddleware
from flask import redirect, render_template
from models import db

@app.route("/rooms")
@AuthenticationMiddleware
def rooms():
    all_room = RoomModel.query.all()
    return render_template("room_related/room_menu.html", **{"room_object": all_room, "room_count": len(all_room)})

@socketio.on("create_room")
def create_room(json, methods=["POST", "GET"]):
    name = json.get("name")

    if name:
        password = json.get("password")
        capacity = json.get("capacity")
        topic = json.get("topic")

        # Save new room data for later display
        current_room = RoomModel(name=name, password=password, topic=topic, capacity=capacity)
        db.session.add(current_room)
        db.session.commit()

        socketio.emit("update_room_list", json, callback=None)
