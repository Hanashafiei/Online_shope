from flask import Blueprint, render_template, request, redirect,url_for,flash
from Models.users import User
from flask_login import login_user
from passlib.hash import sha256_crypt
from extentions import *

user = Blueprint("user", __name__)

@user.route("/user/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("user/login.html")
    else:

        register = request.form.get("register")
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        phone    = request.form.get("phone", "")
        addres  = request.form.get("addres", "")

        if register == "1":
                    new_user=User.query.filter(User.username==username).first()
                    if new_user != None:
                            flash('این نام کاربری قبلا ثبت شده است',"error")
                            return redirect(url_for('user.login'))
                    else:
                        new_user = User(username=username,password=sha256_crypt.hash(password),phone=phone,addres=addres)
                        db.session.add(new_user)
                        db.session.commit()
                        login_user(new_user)
                        return redirect("/user/dashboard")
                
        else:
                     
                     new_user=User.query.filter(User.username==username).first()
                     if new_user == None:
                            flash('نام کاربری نادرست است',"error")
                            return redirect(url_for('user.login'))
                     
                     if sha256_crypt.verify(password,new_user.password):
                            login_user(new_user)
                            return redirect("/user/dashboard")
                     else:
                            flash(' رمز عبور اشتباه است',"error")
                            return redirect(url_for('user.login'))
                            

                            
        

