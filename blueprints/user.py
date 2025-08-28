from flask import Blueprint, render_template, request, redirect,flash
from Models.users import User
from flask_login import login_user
from passlib.hash import sha256_crypt
from extentions import *

user = Blueprint("user", __name__)

@user.route("/user/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("users.html")
    else:

        register = request.form.get("register")
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        phone    = request.form.get("phone", "")
        addres  = request.form.get("addres", "")

        if register != None:
                if phone and phone.isdigit() and len(phone) == 11:
                    new_user = User(username=username,password=sha256_crypt.hash(password),phone=phone,addres=addres)
                    db.session.add(new_user)
                    db.session.commit()
                    login_user(new_user)

                    return redirect("/user/dashboard")
                
                else:
                     flash("شماره تلفن باید دقیقا ۱۱ رقم باشد.", "error")
                     return redirect("/user/login")
        
        return("done")

