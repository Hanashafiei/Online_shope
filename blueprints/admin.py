from flask import Blueprint



admin= Blueprint("admin",__name__)

@admin.route("/admin")
def admin():
    return "this is admin page"

