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

        if not check_valid_session:
            if request.path == url_for("register_view"):
                return func(*args, **kwargs)

            elif request.path != redirect_to:
                return redirect(redirect_to)

            else:
                return func(*args, **kwargs)

        elif (request.path == redirect_to or request.path == url_for("register_view")) and check_valid_session:
            return redirect(url_for("home"))

        else:
            return func(*args, **kwargs)

    return check_session_validity
