import datetime
import json
import string
import random

class Conversation(object):
    def __init__(self, user_id, direction, message):
        self.id = self.string_id_generator()
        self.user_id = user_id
        self.direction = direction
        self.message = message
        self.timestamp = datetime.datetime.now().strftime('%s')

    def string_id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def content_update(self):
        dict_content_update = {}
        if self.user_id != '':
            dict_content_update.update({'user_id': self.user_id})

        if self.direction != '':
            dict_content_update.update({'direction': self.direction})

        if self.message != '':
            dict_content_update.update({'message': self.message})

        return json.dumps(dict_content_update)

    def content(self):
        # convert to json
        return json.dumps({
            'id' : self.id,
            'user_id' : self.user_id,
            'direction' : self.direction,
            'message' : self.message,
            'timestamp' : self.timestamp
        })

    def content_generated(self, dict_conversation):
        dict_conversation['id'] = self.string_id_generator()
        return json.dumps(dict_conversation)
