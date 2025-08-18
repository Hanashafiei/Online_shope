from flask import Blueprint



general= Blueprint("general",__name__)

@general.route("/")
def Home():
    return "this is main"