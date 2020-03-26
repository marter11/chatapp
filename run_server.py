from routes import app, socketio, DEBUG

if __name__ == "__main__":
    socketio.run(app, debug=DEBUG, host="127.0.0.1", port=8000)
