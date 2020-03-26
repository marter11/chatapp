from . import app, render_template

@app.route("/register")
def register_view():
    return render_template("/authentication/register.html")
