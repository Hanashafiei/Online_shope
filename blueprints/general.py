from flask import Blueprint,render_template,request
from sqlalchemy.sql.expression import func
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

    another_products=Product.query.filter(Product.active==1).filter(
        Product.name.like(f'%{product.name[0:3]}%')).order_by(func.rand()).limit(3).all()



    return render_template("product.html",product=product,another_products=another_products)




@general.route("/about")
def about():
    return render_template("about.html")