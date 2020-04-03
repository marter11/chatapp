from routes import app, socketio, DEBUG
import os

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
    socketio.run(app, debug=DEBUG, host="127.0.0.1", port=8000)
