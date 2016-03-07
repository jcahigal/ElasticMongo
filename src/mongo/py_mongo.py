# -*- encoding: utf-8 -*-
'''
Created on 14/01/2016

@author: juanc352 (jchernandez@full-on-net.com)
'''
from __future__ import unicode_literals
from pymongo import MongoClient
from pymongo import ASCENDING

from utils.resources import ElasticMongo
from conn.connector import Connector

NUM_RESULTS = 2


class MongoConnection(Connector):
    '''
    Class to manage the connector with mongoBD
    '''
    db = None

    @staticmethod
    def get_connector():
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

    def get_all(self):
        '''
        Return all elements in mongoDB.

        :return:
            JSON with all documents
        '''
        mongo_con = MongoConnection.get_connector()
        mongo_con.mongo.find()

    def count_all(self):
        '''
        Return the count of docs in mongoDB (op 1).

        :return:
            count of all documents
        '''
        mongo_con = MongoConnection.get_connector()
        return mongo_con.mongo.count()

    def get_to_user(self, user):
        '''
        Get all documents with a particular header To (op 2).

        :args:
            user name of the user

        :return:
            JSON with resulting entries
        '''
        mongo_con = MongoConnection.get_connector()
        res = mongo_con.mongo.find({ElasticMongo.ELASTIC_TYPE_TO: user})
        print res.count
        return res

    def get_word_in_body(self, word):
        '''
        Get all documents with a particular word in its body (op 3).

        :args:
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
        mongo_con = MongoConnection.get_connector()
        # return mongo_con.mongo.find({ElasticMongo.ELASTIC_TYPE_BODY: word}, {ElasticMongo.ELASTIC_TYPE_BODY: 1, "_id": 0})
        res = mongo_con.mongo.find(text_search,
                                   {ElasticMongo.ELASTIC_TYPE_BODY: 1, "_id": 0})
        print res.count
        return res

    def get_word_in_body_complex(self, word, num_results):
        '''
        Get all documents with a particular word in its body (op 4).

        :args:
            word word - to find in body
            num_results - number of results to return

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
        mongo_con = MongoConnection.get_connector()
        res = mongo_con.mongo.find(text_search,
                                   {ElasticMongo.ELASTIC_TYPE_SUBJECT: 1, ElasticMongo.CREATION_LABEL: 1, "_id": 0}
                                   ).sort([(ElasticMongo.CREATION_LABEL, ASCENDING)]
                                          ).limit(num_results)
        print res.count
        return res

    def print_result(self, query, res, num=0):
        '''
        print result for mongo connector

        :args:
            query - name
            res - query results
            num - number of results to print
        '''
        if res:
            total = res.count()
            print "Collections in mongoDB for %s tiene %s resultados." % (query, total)

            if num == 0:
                num_iter = total - 1
            else:
                if num >= total:
                    num_iter = total - 1
                else:
                    num_iter = num

            for i in range(0, num_iter):
                print res[i]
