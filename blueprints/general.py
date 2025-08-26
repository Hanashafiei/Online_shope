from flask import Blueprint,render_template
from Models.product import Product



general= Blueprint("general",__name__)

@general.route("/")
def home():
    products = Product.query.all()
    return render_template("home.html",products=products)


@general.route("/about")
def about():
    return render_template("about.html")