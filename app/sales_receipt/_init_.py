from flask_smorest import Blueprint
from . import routes

bp = Blueprint("sales_receipts", __name__, description="Routes for Sales_Receipts")

