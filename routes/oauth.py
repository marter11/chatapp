from . import app 
from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for
from models.user_model import UserModel, UserModelHandler
from flask.json import jsonify
import os
from hashlib import sha256, md5

client_id = "6798332a937d61eac02a"
client_secret = "517e7dae79c79c1d746155701fbdb1eb2b5ea525"
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'


@app.route("/auth")
def demo():
    """Step 1: User Authorization.

    Redirect the user/resource owner to the OAuth provider (i.e. Github)
    using an URL with a few key OAuth parameters.
    """
    github = OAuth2Session(client_id)
    authorization_url, state = github.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.

@app.route("/callback", methods=["GET"])
def callback():
    """ Step 3: Retrieving an access token.

    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """

    github = OAuth2Session(client_id, state=session['oauth_state'])
    token = github.fetch_token(token_url, client_secret=client_secret,
                               authorization_response=request.url)

    # At this point you can fetch protected resources but lets save
    # the token and show how this is done from a persisted token
    # in /profile.
    session['oauth_token'] = token

    return redirect(url_for('.profile'))


@app.route("/profile", methods=["GET"])
def profile():
    """Fetching a protected resource using an OAuth 2 token.
    """
    github = OAuth2Session(client_id, token=session['oauth_token'])
    user = github.get('https://api.github.com/user').json()
    username = user['login']
    email = user['email']
    hash = sha256(user['node_id'].encode("utf-8")).hexdigest()

    user = UserModel.query.filter_by(username=username).first()
    user_email = UserModel.query.filter_by(email=email).first()

    if(user == None and user_email == None): #CONDITIONS MIGHT HAVE TO BE SEPARATED
        if(email != None):
            handler = UserModelHandler(username, email, hash)
            user = handler.set()
            handler.save(user)

            return redirect('home')
        else:
            #GITHUB ACCOUNT HAS NO PUBLIC EMAIL#

            return redirect('register') #TEMPORARY REDIRECT TO AVOID ERRORS
    else:
        
        #ELSE BLOCK NOT NECESSARY#

        if(user.password == hash):
            return redirect('home') #TEMPORARY REDIRECT TO AVOID ERRORS
        else:
            return redirect('register') #TEMPORARY REDIRECT TO AVOID ERRORS
