from sqlalchemy import*
from extentions import *

class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    description = db.Column(db.String(200), nullable=False, index=True)
    price = db.Column(db.Integer, nullable=False, index=True)
