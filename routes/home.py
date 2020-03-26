from . import app

@app.route("/home")
def home():
    return "<h1>Works!</h1>"
