# application/utils/__init__.py
from flask import Blueprint

database_utils_blueprint = Blueprint('database_utils', __name__)
githubapi_utils_blueprint = Blueprint('githubapi_utils', __name__)

from microservice.utils.database import *
from microservice.utils.githubapi import *