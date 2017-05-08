from flask import Flask
from flask_restful import Api
from components.server.api_conv_user import wrapApiConvUser
from injector import Injector

app = Flask(__name__)
api = Api(app)


inj = Injector('config_task2.json')
convRepo = inj.init_conversationRepo()
userRepo = inj.init_userRepo()
app.register_blueprint(wrapApiConvUser(convRepo, userRepo))

"""
1. What is the advantage of having initialization in configuration file?
- the codes become easy to manage. We don't need to re-initialize object in each file, instead, we can just include
the configuration file.

2. What is this pattern called?
Facade pattern with injectable dependencies

3. If you created a DBStore with path components/store/db_store, what do you need to do to swap the implementation?
- Since it is using term swap. Meaning that the storage system is shifting from the previous memory based storage to database storage.
Having a congiguration file, made this more easy. We can add new array named 'dbStore' under 'components' information, that contains the new path, file, etc.
- Changing the dependecies information of the repo components. The storage memory has already swapped to the new storage system by routing the dependencies from store to dbStore.

"""
if __name__ == "__main__":
    app.run()