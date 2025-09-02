from sqlalchemy import*
from extentions import *
from flask_login import UserMixin

class Payment(db.Model,UserMixin):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True)
    status=Column(String(200),default="pending..")
    price = Column(Integer, nullable=False, index=True)
    cart_id = Column(Integer,ForeignKey("carts.id"), nullable=False,index=True)
    cart=db.relationship('Cart',backref='payments')
    