#!/usr/bin/python3
from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import errors, views
