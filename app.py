from flask import Flask
from extentions import * 
from blueprints.general import general
from blueprints.admin import admin
from blueprints.user import user
import config
from flask_wtf.csrf import CSRFProtect


app=Flask(__name__)
csrf = CSRFProtect(app)
app.debug = True
app.register_blueprint(general)
app.register_blueprint(admin)
app.register_blueprint(user)


app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = config.SECRET_KEY
db.init_app(app)


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()