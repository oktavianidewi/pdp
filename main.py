from flask import Flask
from flask_restful import Api

from components.server.api_conv_user import wrapApiConvUser
from components.repo.conversationRepo import ConversationRepo
from components.repo.userRepo import UserRepo
from components.store.memStore import MemStore

app = Flask(__name__)
api = Api(app)

store = MemStore()
convRepo = ConversationRepo(store)
userRepo = UserRepo(store)

"""
1. Why the type of store is Store and not Memstore?
I am not so clear about this part, which 'Store' is referring to?
'store' here is the instance of Memstore, which is passed to the repository functions as a parameter.

2. What design patterns do you recognize here?
It is a Facade design pattern. Becouse it provides a simple main function wrapping a set of functions behind.
"""

app.register_blueprint(wrapApiConvUser(convRepo, userRepo))


if __name__ == "__main__":
    app.run()