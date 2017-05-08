"""
1) bikin dulu secara terpisah, tidak ada pengecekan ke userid
2) kalau semua method udah bisa, baru bikin pengecekan is_exist userid, supaya data conversation punya userid

"""
import random
import json

class User(object):
    def __init__(self, name, gender, city, phone, email):
        self.id = int(self.int_id_generator())
        self.name = name
        self.gender = gender
        self.city = city
        self.phone = phone
        self.email = email

    def int_id_generator(self):
        return random.randint(0, 100)

    def info_update(self):
        dict_info_update = {}
        if self.name != '':
            dict_info_update.update({'name': self.name})

        if self.gender != '':
            dict_info_update.update({'gender': self.gender})

        if self.city != '':
            dict_info_update.update({'city': self.city})

        if self.phone != '':
            dict_info_update.update({'city': self.phone})

        if self.email != '':
            dict_info_update.update({'city': self.email})

        return json.dumps(dict_info_update)

    def info(self):
        return json.dumps({
            'id' : self.id,
            'name' : self.name,
            'gender' : self.gender,
            'city' : self.city,
            'phone' : self.phone,
            'email' : self.email
        })

    def info_generated(self, dict_user):
        dict_user['id'] = self.int_id_generator()
        return json.dumps( dict_user )