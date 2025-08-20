from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blueprints.general import general
from blueprints.admin import admin
from blueprints.user import user


app=Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(admin)
app.register_blueprint(user)

db=SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost/database"
db.init_app(app)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()