# -*- encoding: utf-8 -*-
'''
Created on 14/01/2016

@author: juanc352 (jchernandez@full-on-net.com)
'''
from __future__ import unicode_literals
from pymongo import MongoClient
from datetime import datetime


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
            print 'creating db'
            MongoConnection.db = client.demo
        return MongoConnection.db


if __name__ == '__main__':
    '''
    Getting time from a simple query of all elements in mongoDB.
    '''
    db = MongoConnection.get_mongo_connector()
    time1 = datetime.now()
    # collection name='elastic_mongo'
    db.elastic_mongo.find()
    time2 = datetime.now()
    result = time2 - time1
    print "MongoDB query time (microseconds): %f" % (result.microseconds)
