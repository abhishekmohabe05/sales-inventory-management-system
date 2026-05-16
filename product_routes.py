from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.extensions import db
from app.models.product import Product
from app.utils import login_required

product_bp = Blueprint("product", __name__, url_prefix="/products")

@product_bp.route("/")
@login_required
def products():
    products = Product.query.all()
    return render_template("products/products.html", products=products)

@product_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_product():
    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        stock_quantity = int(request.form["stock_quantity"])
        product = Product(name=name, price=price, stock_quantity=stock_quantity)
        db.session.add(product)
        db.session.commit()
        flash("Product added successfully!", "success")
        return redirect(url_for("product.products"))
    return render_template("products/add_product.html")

@product_bp.route("/edit/<int:product_id>", methods=["GET", "POST"])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == "POST":
        product.name = request.form["name"]
        product.price = float(request.form["price"])
        product.stock_quantity = int(request.form["stock_quantity"])
        db.session.commit()
        flash("Product updated successfully!", "success")
        return redirect(url_for("product.products"))
    return render_template("products/edit_product.html", product=product)

@product_bp.route("/delete/<int:product_id>", methods=["POST"])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash("Product deleted successfully!", "info")
    return redirect(url_for("product.products"))
