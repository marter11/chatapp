from . import app, RoomModel, socketio, AuthenticationMiddleware, UserModel
from flask import redirect, render_template, request
from models import db

@app.route("/rooms")
@AuthenticationMiddleware
def rooms():
    all_room = RoomModel.query.all()
    session = request.cookies.get("session")
    return render_template("room_related/room_menu.html", **{"room_object": all_room, "room_count": len(all_room), "session": session})

@socketio.on("create_room")
def create_room(json, methods=["POST", "GET"]):
    response = {"code": 404, "message": "Invalid or no user session. Refresh the page and try again!"}
    endpoint = "error" # where to emit
    session = json.get("session")

    if session:
        user = UserModel.query.filter_by(user_key=session).first()

        if user:
            name = json.get("name")

            if name:
                password = json.get("password")
                capacity = json.get("capacity")
                topic = json.get("topic")

                # Save new room data for later display
                current_room = RoomModel(name=name, password=password, topic=topic, capacity=capacity, owner_id=user.id)
                db.session.add(current_room)
                db.session.commit()

                endpoint = "update_room_list"
                response = json

            else:
                response["code"] = 400
                response["message"] = "Invalid or not filled room options!"

    socketio.emit(endpoint, response, callback=None)
