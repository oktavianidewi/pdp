from components.repo.repo import Repo

class ConversationRepo(Repo):
    def __init__(self, mem_store):
        Repo.__init__(self, mem_store)