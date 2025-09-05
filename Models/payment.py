from sqlalchemy import*
from extentions import *
from flask_login import UserMixin

class Payment(db.Model,UserMixin):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True)
    status=Column(String(200),default="pending")
    price = Column(Integer, nullable=False, index=True)
    token= Column(String(36))
    refid= Column(Integer)
    card_pan=Column(String(6))
    transaction_id=Column(Integer)
    date_created=Column(String(15),default=get_current_time)
    cart_id = Column(Integer,ForeignKey("carts.id"), nullable=False,index=True)
    cart=db.relationship('Cart',backref='payments')
    