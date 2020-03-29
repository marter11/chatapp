from . import app, render_template
from models.user_model import UserModel, UserModelHandler
from flask import request, redirect

@app.route("/register", methods=['POST', 'GET'])
def register_view():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if(UserModel.query.filter_by(username=username).first() == None):
            if(UserModel.query.filter_by(email=email).first() == None):
                handler = UserModelHandler(username, email, password)
                user = handler.set()
                handler.save(user)

                return redirect('/login')
            else:
                print("This email is already registered to an existing account.")

                #EXISTING USER WITH THIS EMAIL#

        else:

            #USERNAME TAKEN#

            return redirect('/register')

    return render_template('/authentication/register.html')
