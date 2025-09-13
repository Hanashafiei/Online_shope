from flask import Blueprint,render_template,request
from Models.product import Product



general= Blueprint("general",__name__)

@general.route("/")
def home():
    search=request.args.get('search',None)
    products = Product.query.filter(Product.active==1)
    if search != None:
        products=products.filter(Product.name.like(f'%{search}%'))

    products=products.all()
    return render_template("home.html",products=products,search=search)


@general.route("/product/<int:id>/<name>")
def product(id,name):
    product=Product.query.filter(Product.id==id).filter(Product.name==name).filter(Product.active==1).first_or_404()
    return render_template("product.html",product=product)




@general.route("/about")
def about():
    return render_template("about.html")