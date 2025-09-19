from flask import Blueprint, render_template, request, redirect,url_for,flash,session
from Models.users import User
from Models.cart import Cart
from Models.cart_item import CartItem
from Models.product import Product
from Models.payment import Payment
from flask_login import login_user,login_required,current_user
from passlib.hash import sha256_crypt
from extentions import *
import requests

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
                        return redirect(url_for('user.dashboard'))
                
        else:
                     
                     new_user=User.query.filter(User.username==username).first()
                     if new_user == None:
                            flash('نام کاربری نادرست است',"error")
                            return redirect(url_for('user.login'))
                     
                     if sha256_crypt.verify(password,new_user.password):
                            login_user(new_user)
                            return redirect(url_for('user.dashboard'))
                     else:
                            flash(' رمز عبور اشتباه است',"error")
                            return redirect(url_for('user.login'))



                            
@user.route("/add-to-cart", methods=["GET"])
@login_required
def add_to_cart(): 
       id=request.args.get("id")  
       product=Product.query.filter(Product.id==id).first_or_404()                    
        

       cart=current_user.carts.filter(Cart.status == "pending").first()
       if cart == None:
              cart=Cart()
              current_user.carts.append(cart) 
              db.session.add(cart)

       cart_item=cart.cart_items.filter(CartItem.product==product).first()
       if cart_item==None:

              item=CartItem(quantity=1)  
              item.price=product.price
              item.cart=cart
              item.product=product
              db.session.add(item)

       else:
              cart_item.quantity +=1


       db.session.commit()

       return redirect(url_for('user.cart'))



                            
@user.route("/remove-from-cart", methods=["GET"])
@login_required
def remove_from_cart(): 
       id=request.args.get("id")  
       cart_item=CartItem.query.filter(CartItem.id==id).first_or_404()
       if cart_item.quantity >1:
              cart_item.quantity -=1

       else:
              db.session.delete(cart_item)

       db.session.commit()

       return redirect(url_for('user.cart'))

@user.route("/cart", methods=["GET"])
@login_required
def cart(): 
       cart=current_user.carts.filter(Cart.status=="pending").first()
       return render_template("user/cart.html",cart=cart)      


@user.route("/payment", methods=["GET"])
@login_required
def payment(): 
       cart = current_user.carts.filter(Cart.status == "pending").first()
       r=requests.post('https://sandbox.shepa.com/api/v1/token',
                       data={
                              'api':'sandbox',
                              'amount':cart.total_price(),
                              'callback':'http://localhost:5000/verify'
                              })
       

       token=r.json()["result"]["token"]
       url=r.json()["result"]["url"]
       
       
       pay=Payment(price=cart.total_price(),token=token)
       pay.cart=cart
       
       db.session.add(pay)
       db.session.commit()

       return redirect(url)


@user.route("/verify", methods=["GET"])
@login_required
def verify(): 
    token = request.args.get("token")
    pay = Payment.query.filter(Payment.token == token).first_or_404()

    r = requests.post('https://sandbox.shepa.com/api/v1/verify',
                      data={
                          'api': 'sandbox',
                          'amount': pay.price,
                          'token': token
                      })
    rj = r.json()

    pay_status = str(rj.get("success")).lower() == "true"
    if pay_status:
        result = rj.get("result", {})
        pay.transaction_id = result.get("transaction_id")
        pay.refid = result.get("refid")
        pay.card_pan = result.get("card_pan")
        pay.status = "success"
        pay.cart.status = "paid"
        flash("پرداخت موفق آمیز بود")
    else:
        flash("پرداخت با خطا مواجه شد")
        pay.status = "failed"

    db.session.commit()
    return redirect(url_for('user.dashboard'))


                            
@user.route("/user/dashboard", methods=["GET"])
@login_required
def dashboard(): 
       return render_template("user/dashboard.html")

                            
@user.route("/user/dashboard/order/<id>", methods=["GET"])
@login_required
def order(id): 
       cart=current_user.carts.filter(Cart.id==id).first_or_404()
       return render_template("user/order.html",cart=cart)