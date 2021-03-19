import json

from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_required, login_user, logout_user, current_user

from swoletrics import app, db, login_manager

from forms import WorkoutRoutineForm, LoginForm, SignupForm
from models import User


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template("index.html")


# @app.errorhandler(403)
# def forbidden(e):
#     return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500


