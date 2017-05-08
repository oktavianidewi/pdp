from main_task2 import app
import unittest
import json

class User_test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client(self)

    def tearDown(self):
        pass

    # testing get, checked
    def test_get_user(self):
        id = 1
        response = self.app.get('/users/%s'%id, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # testing post, checked
    def test_create_user(self):
        d_users = {
            'name':'John',
            'gender': 'male',
            'city': 'Jogja',
            'phone': '08174637485',
            'email': 'john@gmail.com',
        }
        response = self.app.post('/users', data=json.dumps(d_users))
        self.assertEqual(response.status_code, 201)
        load_response_layer1 = json.loads(response.data)
        load_response_layer2 = json.loads(load_response_layer1['user']['data'])
        for key in d_users:
            self.assertEqual(d_users[key], load_response_layer2[key])

    # testing for update, checked
    def test_update_user(self):
        id = '109'
        d_users = {
            'id': id,
            'name': 'John Maxwell',
            # 'gender': 'male',
            'city': 'Malang',
            # 'phone': '08174637485',
            # 'email': 'john@gmail.com',
        }
        response = self.app.put('/users/%s'%id, data=json.dumps(d_users))
        self.assertEqual(response.status_code, 201)
        """
        for key in load_response['user']['data']:
            self.assertEqual(d_users[key], load_response['user']['data'][key])
        """

    # testing delete, checked
    def test_delete(self):
        id = 'fhj'
        response = self.app.delete('/users/%s' % id)
        self.assertEqual(response.status_code, 200)

    # testing list all, checked
    def test_get_all_users(self):
        page = 2
        limit = 3
        response = self.app.get('/users/?page=%d&limit=%d' % (page, limit))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()