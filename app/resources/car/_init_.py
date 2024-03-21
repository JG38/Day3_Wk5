from flask_smorest import Blueprint
from . import routes

bp = Blueprint('cars', __name__, description="Routes for cars")

