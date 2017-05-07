# from flask import app
from api_conv_user import app
import unittest
import json

class Conversation_test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    def tearDown(self):
        pass

    # testing get, checked
    def test_get_conversation(self):
        id = 1
        response = self.app.get('/conversations/%s'%id, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # testing post, checked
    def test_create_conversation(self):
        d_conversations = {
            "id":"2",
            "user_id":"109",
            "direction": "outcoming",
            "message": "testing description",
        }
        response = self.app.post('/conversations', data=json.dumps(d_conversations)) # , headers={'Content-Type':'application/json')}
        self.assertEqual(response.status_code, 201)
        load_response_layer1 = json.loads(response.data)
        load_response_layer2 = json.loads( load_response_layer1['conversation']['data'] )
        for key in d_conversations:
            self.assertEqual(d_conversations[key], load_response_layer2[key])

    # testing for update, checked
    def test_update_conversation(self):
        id = '2'
        d_conversations = {
            'id': id,
            # 'user_id': '101',
            'direction': 'incoming',
            # 'message': 'testing description',
        }
        print 'id %s'%id
        response = self.app.put('/conversations/%s'%id, data=json.dumps(d_conversations))
        # , headers={'Content-Type':'application/json')}
        # load_response_layer1 = json.loads(response.data)
        # print load_response_layer1
        self.assertEqual(response.status_code, 201)

    # testing delete, checked
    def test_delete(self):
        id = '2'
        response = self.app.delete('/conversations/%s' % id)
        self.assertEqual(response.status_code, 200)


    # testing list all, checked
    def test_get_all_conversations(self):
        page = 2
        limit = 3
        response = self.app.get('/conversations/?page=%d&limit=%d' % (page, limit))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()