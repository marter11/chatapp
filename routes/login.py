from . import app, render_template
from models.user_model import UserModel, UserModelHandler
from flask import request, redirect
from hashlib import sha256, md5


@app.route("/login", methods=['POST', 'GET'])
def login_view():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = UserModel.query.filter_by(username=username).first()
        hash = sha256(password.encode("utf-8")).hexdigest()
        if(user != None):
            if(user.password == hash):
                return redirect('/home')
            else:

                #WRONG PASSWORD#

                print('Wrong password!')
        else:

            #WRONG USERNAME#

            return redirect('/register')

    return render_template("/authentication/login.html")