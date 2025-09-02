from sqlalchemy import*
from sqlalchemy.orm import backref
from extentions import *
from flask_login import UserMixin

class Cart(db.Model,UserMixin):
    __tablename__ = "carts"
    
    id = Column(Integer, primary_key=True)
    status=Column(String(200),default="pending..")
    user_id = Column(Integer,ForeignKey('users.id'), nullable=False,index=True)
    user=db.relationship('User',backref=backref('carts',lazy='dynamic'))


    def total_price(self):
        total=0
        for item in self.cart_items:
            t=item.price * item.quantity
            total += t
        return total

    