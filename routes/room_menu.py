from . import app, render_template, RoomModel, socketio

@app.route("/rooms")
def rooms():
    all_room = RoomModel.query.all()
    return render_template("room_related/room_menu.html", **{"room_object": all_room, "room_count": len(all_room)})

@socketio.on("create_room")
def create_room(json, methods=["POST", "GET"]):
    if json.get("name"):
        socketio.emit("update_room_list", json, callback=None)
