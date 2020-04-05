from flask import request, redirect, make_response, url_for, render_template
from . import app, AuthenticationMiddleware
from models.user_model import UserModel, UserModelHandler
from hashlib import sha256, md5

@app.route("/login", methods=['POST', 'GET'])
@AuthenticationMiddleware
def login_view():
    response = make_response(render_template("/authentication/login.html"))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = UserModel.query.filter_by(username=username).first()
        hash = sha256(password.encode("utf-8")).hexdigest()

        if user != None:
            if user.password == hash:

                # Set new session every login
                new_user_session_key = UserModelHandler.generate_user_key(username)
                user.user_key = new_user_session_key
                UserModelHandler.save(user)

                response =  make_response(redirect('/home'))
                response.set_cookie("session", user.user_key, max_age=5000)
            else:
                print('Wrong password!')
        else:
            return render_template("/authentication/login.html", nouser=True)

    return response
