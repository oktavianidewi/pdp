"""
1) bikin dulu secara terpisah, tidak ada pengecekan ke userid
2) kalau semua method udah bisa, baru bikin pengecekan is_exist userid, supaya data conversation punya userid

"""
import datetime
import json

class User:
    def __init__(self, id, name, gender, city, phone, email):
        self.id = str(id)
        self.name = str(name)
        self.gender = gender
        self.city = city
        self.phone = phone
        self.email = email

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
        # convert to json
        # checking is_array, if yes convert to json
        return json.dumps({
            'id' : self.id,
            'name' : self.name,
            'gender' : self.gender,
            'city' : self.city,
            'phone' : self.phone,
            'email' : self.email
        })