# from flask import Blueprint, render_template, session
# from app.utils import login_required

# dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

# @dashboard_bp.route("/")
# @login_required
# def dashboard():
#     return render_template("dashboard/dashboard.html", username=session.get("username"))


from flask import Blueprint, render_template, session
from app.utils import login_required

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard_bp.route("/")
@login_required
def dashboard():
    username = session.get("username", "User")

    # Dummy data (you can connect DB later)
    total_products = 50
    total_sales = 12000
    today_sales = 2000
    low_stock = 5

    return render_template(
        "dashboard/dashboard.html",
        username=username,
        total_products=total_products,
        total_sales=total_sales,
        today_sales=today_sales,
        low_stock=low_stock
    )