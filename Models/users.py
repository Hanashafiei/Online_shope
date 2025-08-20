from sqlalchemy import*

class User(db.Model):
    __tablename__="users"
    id=column()
    