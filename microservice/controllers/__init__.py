# application/controllers/__init__.py
from flask import Blueprint

user_controller_blueprint = Blueprint('user_controller', __name__)
github_controller_blueprint = Blueprint('github_controller', __name__)


from microservice.controllers.user_controller import *
from microservice.controllers.github_controller import *