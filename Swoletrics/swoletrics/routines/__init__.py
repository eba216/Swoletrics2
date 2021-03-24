from flask import Blueprint

routines = Blueprint('routines', __name__)

from . import views