from flask import Blueprint,render_template,request,session,redirect,abort
from config import *



admin= Blueprint("admin",__name__)

@admin.route("/admin/login",methods=["POST" , "GET"])
def login():
    if request.method == "POST":
        username=request.form.get('username',None)
        password=request.form.get('password',None)

        if username ==ADMIN_USERNAME and password==ADMIN_PASSWORD:
            session["admin_login"]=username
            return redirect("/admin/dashboard")
        
        else:
            return render_template("admin/login.html")
        
    return render_template("admin/login.html")


@admin.route("/admin/dashboard",methods=["GET"])
def dashboard():
    if session.get("admin_login",None) == None:
        abort(403)
    else:
        return"this is dash"
    




