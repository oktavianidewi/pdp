from flask import Flask
from flask_restful import Api
from components.server.api_conv_user import wrapApiConvUser
from injector import Injector

app = Flask(__name__)
api = Api(app)


inj = Injector('config_task3.json')
convRepo = inj.init_genericRepo('conversation')
userRepo = inj.init_genericRepo('user')
app.register_blueprint(wrapApiConvUser(convRepo, userRepo))


if __name__ == "__main__":
    app.run()