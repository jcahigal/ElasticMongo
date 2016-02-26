'''
Created on 08/01/2016

Module to load the data in ES and mongoBD.

Mongo
-------
* database 'demo', collection 'mongo'.
* Clean collections with db.mongo.drop()


ElasticSearch
--------------
* index 'demo', type 'elastic'
* drop index with: curl -X DELETE "http://localhost:9200/demo/"

@author: juanc352 (jchernandez@full-on-net.com)
'''

from __future__ import unicode_literals
from mongo.py_mongo import MongoConnection
from es.elastic_search import ElasticConnection
from resources import ElasticMongo
from datetime import datetime
from datetime import timedelta
import random
from random import randrange
import argparse

CREATION_LABEL = "creation"


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

if __name__ == '__main__':
    '''
    Inserting N new entries.
    '''

    # reading args
    parser = argparse.ArgumentParser(description='loader of data in mongoDB')
    parser.add_argument('--number',
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

    # it simulate a creation date for new entries
    start_date = datetime.strptime('01/01/2013 0:30', '%d/%m/%Y %H:%M')
    end_date = datetime.strptime('31/12/2015 11:55', '%d/%m/%Y %H:%M')

    # inserting
    time1 = datetime.now()
    for i in range(0, args.n_entries):
        random.seed(datetime.now().microsecond)
        entry_index = random.randint(0, total_entries - 1)

        creation_date = random_date(start_date, end_date)
        new_entry = ElasticMongo.entries[entry_index]
        new_entry[CREATION_LABEL] = creation_date

        if args.system == "B" or args.system == "M":
            # mongo

            # db.elastic_mongo.insert_one(ElasticMongo.entries[entry_index])
            db.mongo.update({'to_force_insert': "duplcate_entries"}, new_entry, upsert=True)

        if args.system == "B" or args.system == "E":
            # elastic
            es.index(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE, body=new_entry)

    time2 = datetime.now()
    result = time2 - time1
    print "insert time (microseconds): %f" % (result.microseconds)
