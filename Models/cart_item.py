from sqlalchemy import*
from sqlalchemy.orm import backref
from extentions import *
from flask_login import UserMixin

class CartItem(db.Model,UserMixin):
    __tablename__ = "cart_items"
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer,ForeignKey('products.id'), nullable=False,index=True)
    cart_id = Column(Integer,ForeignKey('carts.id'), nullable=False,index=True)
    quantity = Column(Integer)
    price = db.Column(db.Integer, nullable=False, index=True)
    product=db.relationship('Product',backref='cart_items')
    cart=db.relationship('Cart',backref=backref('cart_items', lazy='dynamic'))
    