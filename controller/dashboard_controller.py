from flask import Blueprint, render_template

dashboard = Blueprint('dashboard_controller', __name__)


@dashboard.route('/')
def login_view():
    return render_template("index.html")
