"Documentation"

import requests
import logging
import json

ES_HOST_NAME = '52.4.196.153'
ES_PORT = 9200
ES_INDEX = 'testtest1'

# ES_HOST_NAME = 'localhost'
# ES_PORT = 9200
# ES_INDEX = 'testtest1'


def dummy_obj(name):
    a = Data(1, 'name', 'geo', 'ref', 'Kanari yabai', 'Sugoi kara', 'Restaulant')
    return a

class Data(object):
    def __init__(self, id, name, geo, reference, probability, reason, genre):
        self.id = id
        self.name = name
        self.geo = geo
        self.reference = reference
        self.probability = probability
        self.reason = reason
        self.genre = genre

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' : ' + self.reason

    def put(self):
        logging.info(str(self.__dict__))
        payload = json.dumps(self.__dict__)
        logging.info('http://' + ES_HOST_NAME + ':' + str(ES_PORT) + '/' + ES_INDEX)
        logging.info(str(payload))
        r = requests.post('http://' + ES_HOST_NAME + ':' + str(ES_PORT) + '/' + ES_INDEX, data=payload)