from flask import Flask
from blueprints.general import general
from blueprints.admin import admin
from blueprints.user import user


app=Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(admin)
app.register_blueprint(user)



if __name__ == '__main__':
    app.run()