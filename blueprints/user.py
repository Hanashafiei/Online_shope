from flask import Blueprint,render_template
import Models.users



user= Blueprint("user",__name__)

@user.route("/user/login")
def user_page():
    return render_template("users.html")
