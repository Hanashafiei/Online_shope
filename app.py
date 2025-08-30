from flask import Flask
from extentions import * 
from blueprints.general import general
from blueprints.admin import admin
from blueprints.user import user
import config
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from Models.users import User


app=Flask(__name__)
csrf = CSRFProtect(app)
login_manager = LoginManager()
app.debug = True
app.register_blueprint(general)
app.register_blueprint(admin)
app.register_blueprint(user)


app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = config.SECRET_KEY
db.init_app(app)
login_manager.init_app(app)


with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id==user_id).first()


if __name__ == '__main__':
    app.run(host='0.0.0.0')