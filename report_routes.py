from flask import Blueprint, render_template
from app.models.product import Product
from app.models.sale import Sale
from app.utils import login_required

report_bp = Blueprint("report", __name__, url_prefix="/reports")

@report_bp.route("/")
@login_required
def reports():
    products = Product.query.all()
    sales = Sale.query.all()
    return render_template("reports/reports.html", products=products, sales=sales)
