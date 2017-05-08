import json

class MemStore():
    def __init__(self):
        self.items = []

    # it works like push
    def store(self, item, idx=None):
        # self.items.append(item)
        if idx == None:
            self.items.append(item)
            stored_data = item
        else:
            load_item_layer1 = json.loads(item)
            print "id   ", idx
            for key in load_item_layer1:
                load_item_layer2 = json.loads(self.items[idx])
                load_item_layer2[key] = load_item_layer1[key]
            self.items.insert(idx, load_item_layer2)
            stored_data = load_item_layer2
        return stored_data

    # deletes data based on id
    def pop(self, id):
        idx = self.idtoidx(id)
        return self.items.pop(idx)

    def idtoidx(self, id):
        for index, datum in enumerate(self.items):
            datum_id = json.loads(datum)["id"]
            if (datum_id == str(id)):
                return index

    def findbyidx(self, idx):
        return self.items[idx]

    def find(self, id):
        index = self.idtoidx(id)
        if index is None:
            return None
        else:
            return self.items[index]


    # loads all data
    def loads(self):
        return self.items

    def used_memory_len(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0