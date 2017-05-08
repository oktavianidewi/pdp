import os
import json

from components.repo.conversationRepo import ConversationRepo
from components.repo.genericRepo import GenericRepo
from components.repo.userRepo import UserRepo
from components.store.memStore import MemStore

class Injector(object):
    def __init__(self, config_file):
        self.config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), config_file))
        self.init_obj = None
        self.schema = None

    def load_config_file(self):
        f = open(self.config_file, 'r')
        config = json.load(f)
        return config

    def get_component_dependecies_byname(self, keyname):
        components = self.load_config_file()['components']
        return components[keyname]['dependencies']

    def get_memoryStore(self):
        dependencies = self.get_component_dependecies_byname('store')
        if len(dependencies) == 0:
            self.init_obj = MemStore()
        return self.init_obj

    def init_conversationRepo(self):
        dependencies = self.get_component_dependecies_byname('convRepo')
        if len(dependencies) == 0:
            self.init_obj = ConversationRepo()
        else:
            for dependency in dependencies:
                if dependency == 'store':
                    self.init_obj = ConversationRepo(self.get_memoryStore())
        return self.init_obj

    def init_userRepo(self):
        dependencies = self.get_component_dependecies_byname('userRepo')
        if len(dependencies) == 0:
            self.init_obj = UserRepo()
        else:
            for dependency in dependencies:
                if dependency == 'store':
                    self.init_obj = UserRepo(self.get_memoryStore())
        return self.init_obj


    def init_genericRepo(self, type):
        dependencies = self.get_component_dependecies_byname('convRepo')
        if type =='conversation':
            self.schema = self.load_config_file()['components']['convRepo']['options']['schema']
        elif type == 'user':
            self.schema = self.load_config_file()['components']['userRepo']['options']['schema']

        if len(dependencies) == 0:
            self.init_obj = GenericRepo()
        else:
            for dependency in dependencies:
                if dependency == 'store':
                    self.init_obj = GenericRepo(self.get_memoryStore(), self.schema)
        return self.init_obj

# inj = Injector('config_task3.json')
# inj.get_genericRepo('conversation')