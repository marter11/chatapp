from . import app, render_template

@app.route("/login")
def login_view():
    return render_template("/authentication/login.html")
