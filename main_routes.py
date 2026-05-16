from flask import Blueprint, render_template, redirect, url_for

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    # Option A: show a homepage
    return render_template("index.html")

    # Option B: if you prefer redirect straight to login, use this instead:
    # return redirect(url_for("auth.login"))
