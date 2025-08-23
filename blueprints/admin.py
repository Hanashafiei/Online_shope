from flask import Blueprint,render_template



admin= Blueprint("admin",__name__)

@admin.route("/admin/login")
def login():
    return render_template("admin/login.html")

