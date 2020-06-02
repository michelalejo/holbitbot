#!/usr/bin/python3
from flask import Flask, render_template
from flask import request, redirect, session
from os import environ
import uuid
from api.oauth import Oauth

cache_id = uuid.uuid4()
app = Flask(__name__)

@app.route('/home', strict_slashes=False)
def home():
    """Home page"""
    return render_template('index.html', cache_id=cache_id)

@app.route("/log", methods = ["get"])
def index():
    return redirect(Oauth.discord_login_url)

@app.route("/login", methods = ["get"])
def login():
    code = request.args.get("code")
    return code

if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port=5000, debug=True)
