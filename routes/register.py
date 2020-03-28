from . import app, render_template
from models.user_model import UserModel, UserModelHandler
from flask import request, redirect

@app.route("/register", methods=['POST', 'GET'])
def register_view():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        handler = UserModelHandler(username, email, password)
        user = handler.set()
        handler.save(user)
        
        return redirect('/login')

    return render_template('/authentication/register.html')
