from routes import app, socketio, DEBUG
import sys
import os

# Deletes all current data from the db automatically
if "--reset-db" in sys.argv and DEBUG:
    from models import db
    db.drop_all()
    db.create_all()

elif __name__ == "__main__":
    app.secret_key = os.urandom(24)
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
    socketio.run(app, debug=DEBUG, host="127.0.0.1", port=8000)
