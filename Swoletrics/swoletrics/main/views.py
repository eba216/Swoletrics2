from flask import render_template, redirect, url_for, flash
from flask_login import login_required

from . import main
from .. import login_manager
from ..models import User
from ..auth.forms import SignupForm
from .. import db


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@main.route('/index', methods = ["GET", "POST"])
@main.route('/', methods = ["GET", "POST"])
def index():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash(f"Welcome, {user.username}! Please login.")
        return redirect(url_for('auth.login'))
    return render_template("index.html", form=form)

@login_required
@main.route('/user/<username>', methods = ["GET", "POST"])
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user = user)

# @main.app_errorhandler(403)
# def forbidden(e):
#     return render_template('403.html'), 403
#

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


