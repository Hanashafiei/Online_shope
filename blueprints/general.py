from flask import Blueprint,render_template



general= Blueprint("general",__name__)

@general.route("/")
def home():
    return render_template("home.html")


@general.route("/about")
def about():
    return render_template("about.html")