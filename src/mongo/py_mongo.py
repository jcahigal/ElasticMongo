# -*- encoding: utf-8 -*-
'''
Created on 14/01/2016

@author: juanc352 (jchernandez@full-on-net.com)
'''
from __future__ import unicode_literals
import argparse
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
        Return the count of docs in mongoDB.

        :args:
            mongo_con MongoDB connector

        :return:
            count of all documents
        '''
        return mongo_con.mongo.count()

    @staticmethod
    def get_to_user(mongo_con, user):
        '''
        Get all documents with a particular header To.

        :args:
            mongo_con MongoDB connector
            user name of the user

        :return:
            JSON with resulting entries
        '''
        return mongo_con.mongo.find({"headers.To": user})


if __name__ == '__main__':
    '''
    Getting time from different mongo operations
    '''
    # reading args
    parser = argparse.ArgumentParser(description='Demo launcher',
                                     add_help='execute this script with only one integer argument: the number on entries')
    parser.add_argument('--operation',
                        '-o',
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
        for to in tos:
            print to