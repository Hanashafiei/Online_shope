from flask import Blueprint
import Models.users



user= Blueprint("user",__name__)

@user.route("/user")
def user_page():
    return "this is user page"
