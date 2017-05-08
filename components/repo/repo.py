class Repo(object):
    def __init__(self, mem_store):
        self.cache = mem_store

    def response_message(self, response, data):
        return {'data': data, 'response':response}

    def create(self, data):
        try:
            insert = self.cache.store(data)
            result = self.response_message(True, data)
        except:
            result = self.response_message(False, 'Fail to store data.')
        return result
        # return self.cache.store(data)

    def get_all(self):
        try:
            data = self.cache.loads()
            result = self.response_message(True, data)
        except self.cache.is_empty():
            result = self.response_message(False, 'No data found.')
        return result

    def get(self, id):
        findbyid = self.cache.find(id)
        if findbyid:
            result = self.response_message(True, findbyid)
        else:
            result = self.response_message(False, 'ID is not found')
        return result
        # return

    def list(self, page, limit):
        load_data = self.cache.loads()
        length_data = self.cache.used_memory_len()

        paging_data = {}

        if length_data > 0 :
            if page*limit > length_data:
                page = (length_data // limit)+1

            for i in range(page):
                list_data = []
                for j in range(i * limit, ((i + 1) * limit)):
                    try:
                        list_data.append(load_data[j])
                    except:
                        pass
                paging_data[i] = list_data
            result = paging_data
        else:
            result = self.response_message(False, 'Empty memory')
        return result

    def update(self, id, updated_data):
        """ """
        idx = self.cache.idtoidx(id)

        if idx is not None:
            new_data = updated_data
            update = self.cache.store(new_data, idx)
            result = self.response_message(True, update)
        else:
            result = self.response_message(False, 'ID is not found')
        return result

    def remove(self, id):
        get_id = self.get(id)

        if get_id['response']:
            delete = self.cache.pop(id)
            result = self.response_message(True, delete)
        else:
            result = self.response_message(False, 'Error')
        return result