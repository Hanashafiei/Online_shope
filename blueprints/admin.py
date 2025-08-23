from flask import Blueprint,render_template,request
from config import *



admin= Blueprint("admin",__name__)

@admin.route("/admin/login",methods=["POST" , "GET"])
def login():
    if request.method == "post":
        username=request.form.get('username',None)
        password=request.form.get('password',None)

        if username ==ADMIN_USERNAME and password==PASSWORD_USERNAME:
            pass



    else:
        return render_template("admin/login.html")

