#!/usr/bin/python3
from flask import Blueprint

main = Blueprint('main', __name__)

from . import errors, views