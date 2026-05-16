from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.extensions import db
from app.models.product import Product
from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.utils import login_required

sales_bp = Blueprint("sales", __name__, url_prefix="/sales")

@sales_bp.route("/", methods=["GET", "POST"])
@login_required
def sales():
    products = Product.query.all()
    if request.method == "POST":
        product_id = int(request.form["product_id"])
        quantity = int(request.form["quantity"])
        product = Product.query.get_or_404(product_id)

        if product.stock_quantity < quantity:
            flash("Not enough stock!", "danger")
            return redirect(url_for("sales.sales"))

        product.stock_quantity -= quantity
        sale = Sale(total_amount=product.price * quantity)
        db.session.add(sale)
        db.session.commit()

        sale_item = SaleItem(sale_id=sale.id, product_id=product.id, quantity=quantity, price=product.price)
        db.session.add(sale_item)
        db.session.commit()

        flash("Sale completed successfully!", "success")
        return redirect(url_for("sales.sales"))

    return render_template("sales/sales.html", products=products)
