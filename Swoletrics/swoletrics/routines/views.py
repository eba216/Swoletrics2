from . import routines
from flask import render_template, redirect, url_for, flash
from flask_login import login_required

from ..main import views
from .. import login_manager
from ..models import User


@login_required
@routines.route('/<username>', methods=["GET", "POST"])
def routines(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('routines.html', user=user)