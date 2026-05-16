from flask import flash
from app.models.product import Product

def flash_low_stock_notifications(products):
    for product in products:
        if product.stock_quantity < 5:
            flash(f"Low stock alert: {product.name}", "warning")
