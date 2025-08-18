from flask import Blueprint



general= Blueprint("general",__name__)

@general.route("/")
def home():
    return "this is main"


@general.route("/about")
def about():
    return "about us"