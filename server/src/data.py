"Documentation"

import logging
import random
from elasticsearch import Elasticsearch
from datetime import datetime

ES_INDEX = 'ep_venues'
ES_TYPE = 'venue'

# Returns dummy data for testing ES manipulation
def dummy_obj(name):
    rx = random.random() / 500
    ry = random.random() / 500
    a = Data(1, name, [35.6585 + rx, 139.7013 + ry],
             'http://docs.python.jp/2/tutorial/interpreter.html',
             'http://blog-imgs-19.fc2.com/d/e/v/devenirherbe/saiboku_buta.jpg',
             random.random(),
             'Sugoi kara', 'Washoku Resutoran')
    return a

# FIXME: Please rename me! Refactoring!
# FIXME: How do we want to generate id? some hashing? Want to put a same id for same instance,
#        even they have different name. Probably better to use geo info?
class Data(object):
    def __init__(self, instance_id, name, geo, reference_url, reference_picture, probability, reason, genre):
        self.instance_id = instance_id
        self.name = name
        self.geo = geo
        self.reference_url = reference_url
        self.reference_picture = reference_picture
        self.probability = probability
        self.reason = reason
        self.genre = genre
        self.bookmarked = False
        self.timestamp = datetime.now()

    def __str__(self):
        return str(self.__dict__)

    def put(self):
        print 'a'
        es = Elasticsearch([
            # {'host': 'localhost'},
            {'host': '52.4.196.153', 'port': 9200},
            ])
        print 'a'
        es.indices.create(index=ES_INDEX, ignore=400)
        es.index(index=ES_INDEX, doc_type=ES_TYPE, body=self.__dict__)
        logging.info(str(self.__dict__) + ' was added.')
