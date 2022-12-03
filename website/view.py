from flask import Blueprint, render_template

view = Blueprint('view', __name__)

@view.route('/')
def home():
    return render_template("home.html")

@view.route('/')
def login():
    return render_template("login.html")

@view.route('/')
def signup():
    return render_template("signup.html")
