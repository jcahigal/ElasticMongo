'''
Created on 08/01/2016

Module to load the data in ES and mongoBD.

Mongo
-------
* database 'demo', collection 'mongo'.
* Clean collections with db.elastic_mongo.drop()es


ElasticSearch
--------------
* index 'demo', type 'elastic'

@author: juanc352 (jchernandez@full-on-net.com)
'''

from __future__ import unicode_literals
from mongo.py_mongo import MongoConnection
from es.elastic_search import ElasticConnection
from resources import ElasticMongo
from datetime import datetime
import random
import argparse


if __name__ == '__main__':
    '''
    Inserting N new entries.
    '''

    # reading args
    parser = argparse.ArgumentParser(description='loader of data in mongoDB',
                                     add_help='execute this script with only one integer argument: the number on entries')
    parser.add_argument( '--number',
                        '-n',
                        dest='n_entries',
                        type=int,
                        help='number of new entries to be created',
                        required=True)
    parser.add_argument('--system',
                        '-s',
                        dest='system',
                        default='B',
                        choices=['M', 'E', 'B'],
                        help='"M": mongo, "E": elastic or "B": both(default)',
                        required=False)
    args = parser.parse_args()

    db = MongoConnection.get_mongo_connector()
    total_entries = len(ElasticMongo.entries)
    es = ElasticConnection.get_elastic_connector()

    # inserting
    time1 = datetime.now()
    for i in range(0, args.n_entries):
        random.seed(datetime.now().microsecond)
        entry_index = random.randint(0, total_entries - 1)

        if args.system == "B" or args.system == "M":
            # mongo
            # db.elastic_mongo.insert_one(ElasticMongo.entries[entry_index])
            db.mongo.update({'to_force_insert': "duplcate_entries"}, ElasticMongo.entries[entry_index], upsert=True)

        if args.system == "B" or args.system == "E":
            # elastic
            es. index(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE, body=ElasticMongo.entries[entry_index])

    time2 = datetime.now()
    result = time2 - time1
    print "insert time (microseconds): %f" % (result.microseconds)