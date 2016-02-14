# -*- encoding: utf-8 -*-
'''
Created on 14/01/2016

@author: juanc352 (jchernandez@full-on-net.com)
'''
from __future__ import unicode_literals
import argparse
from pymongo import MongoClient
from datetime import datetime
from utils.resources import ElasticMongo


class MongoConnection(object):
    '''
    Class to manage the connector with mongoBD
    '''
    db = None

    @staticmethod
    def get_mongo_connector():
        '''
        Function to create a mongoDB connector to one DB.

        :return:
            db connector
        '''
        if not MongoConnection.db:
            client = MongoClient()
            # DB name='demo'
            print 'creating mongo connector'
            MongoConnection.db = client.demo
        return MongoConnection.db

    @staticmethod
    def get_all(mongo_con):
        '''
        Return all elements in mongoDB.

        :args:
            mongo_con MongoDB connector

        :return:
            JSON with all documents
        '''
        mongo_con.mongo.find()

    @staticmethod
    def count_all(mongo_con):
        '''
        Return the count of docs in mongoDB (op 1).

        :args:
            mongo_con MongoDB connector

        :return:
            count of all documents
        '''
        return mongo_con.mongo.count()

    @staticmethod
    def get_to_user(mongo_con, user):
        '''
        Get all documents with a particular header To (op 2).

        :args:
            mongo_con MongoDB connector
            user name of the user

        :return:
            JSON with resulting entries
        '''
        return mongo_con.mongo.find({ElasticMongo.ELASTIC_TYPE_TO: user})

    @staticmethod
    def get_word_in_body(mongo_con, word):
        '''
        Get all documents with a particular word in its body (op 3).

        :args:
            mongo_con ElastisSearch connector
            word word to find in body

        :return:
            Mongo bodies resulting documents
        '''

        text_search = {
                      "$text":
                        {
                          "$search": word,
                          "$caseSensitive": False,
                          "$diacriticSensitive": False
                        }
                    }
        #return mongo_con.mongo.find({ElasticMongo.ELASTIC_TYPE_BODY: word}, {ElasticMongo.ELASTIC_TYPE_BODY: 1, "_id": 0})
        return mongo_con.mongo.find(text_search,
                                    {ElasticMongo.ELASTIC_TYPE_BODY: 1, "_id": 0})



if __name__ == '__main__':
    '''
    Getting time from different mongo operations
    '''
    # reading args
    parser = argparse.ArgumentParser(description='Demo launcher',
                                     add_help='execute this script with only one integer argument: the number on entries')
    parser.add_argument('--operation',
                        '-op',
                        dest='op',
                        type=int,
                        help='index of the operation to run, 0 to all',
                        required=True)
    args = parser.parse_args()

    # getting mongo connector
    db = MongoConnection.get_mongo_connector()

    if args.op == 0 or args.op == 1:
        # count
        time1 = datetime.now()
        total = MongoConnection.count_all(db)
        time2 = datetime.now()
        result = time2 - time1
        print "MongoDB query time (microseconds): %f" % (result.microseconds)
        print "Mongo count: %s" % (total)

    elif args.op == 0 or args.op == 2:
        # getting docs with a mail in 'to' list
        to_user = 'steven.kean@enron.com'
        time1 = datetime.now()
        tos = MongoConnection.get_to_user(db, to_user)
        time2 = datetime.now()
        result = time2 - time1
        print "MongoDB query time (microseconds): %f" % (result.microseconds)
        print "Collections in mongo with %s header to %s" % (to_user, tos.count())
        if tos.count > 0:
            print tos[0]

    if args.op == 0 or args.op == 3:
        # getting docs with a word in body
        word_body = 'humongous'
        time1 = datetime.now()
        bodies = MongoConnection.get_word_in_body(db, word_body)
        time2 = datetime.now()
        result = time2 - time1
        print "ElastisSearch query time (microseconds): %f" % (result.microseconds)
        print "collections in mongo with %s word in its body %s" % (word_body, bodies.count())
        if bodies.count > 0:
            print bodies[0]
