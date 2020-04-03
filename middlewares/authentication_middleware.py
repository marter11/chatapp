from flask import redirect, request, url_for
from functools import wraps
from . import UserModel

# Check if user is already authenticated
def AuthenticationMiddleware(func):

    # Handle returned function as base object
    @wraps(func)
    def check_session_validity(*args, **kwargs):
        session_cookie = request.cookies.get("session")
        check_valid_session = UserModel.query.filter_by(user_key=session_cookie).first()
        redirect_to = url_for("login_view")

        if request.path != redirect_to and not check_valid_session:
            return redirect(redirect_to)

        elif request.path == redirect_to and check_valid_session:
            return redirect(url_for("home"))

        else:
            return func(*args, **kwargs)

    return check_session_validity
