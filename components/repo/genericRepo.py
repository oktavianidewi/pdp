from components.repo.repo import Repo
from components.repo.conversation import Conversation
from components.repo.user import User
import json

class GenericRepo(Repo, Conversation, User):
    def __init__(self, mem_store, schema):
        Repo.__init__(self, mem_store)
        self.schema = schema