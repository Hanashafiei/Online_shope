from sqlalchemy import*
from extentions import *
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(100),unique=True, nullable=False,index=True)
    password = Column(String(50), nullable=False,index=True)
    phone = Column(String(11),nullable=False,index=True)
    addres= Column(String(200),nullable=False,index=True)