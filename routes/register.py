from . import app, render_template
from models.user_model import UserModel, UserModelHandler
from flask import request

@app.route("/register", methods=['POST'])
def register_view():
    return render_template("/authentication/register.html")

def UserReg():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        UserModelHandler(username, email, password)
        UserModelHandler.set()
        UserModelHandler.save()