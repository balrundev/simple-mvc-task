from multiprocessing.sharedctypes import Value
import re
from collections import OrderedDict

class Client:
    def __init__(self, first_name: str, last_name: str, email: str, city: str, postal_code: str, address: str):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        for el in [first_name, last_name, city, address]:
            if not el.strip():
                raise ValueError('Заполните все поля')
        if not postal_code.isnumeric():
            raise ValueError('Указан неверный индекс')
        if not re.fullmatch(email_regex, email):
            raise ValueError('Указан неверный e-mail')
        
        self.__client = OrderedDict({
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'city': city,
            'postal_code': postal_code,
            'address': address
        })

    @property
    def client(self):
        return self.__client

    @property
    def data(self):
        return list(self.__client.values())
