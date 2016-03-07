# -*- encoding: utf-8 -*-
'''
Created on 01/03/2016

@author: juanc352 (jchernandez@full-on-net.com)
'''

from __future__ import unicode_literals

import argparse
from datetime import datetime

from es.elastic_search import ElasticConnection
from mongo.py_mongo import MongoConnection

NUM_RESULTS = 2


class ConnectorFactory(object):
    '''
    Class to instantiate the different connectors supported
    '''

    connectors = ['E', 'M']

    @staticmethod
    def create_connector(conn_type):
        '''
        Instantiate a connector

        :args:
        conn_type - 'E' for elastic or 'M' for mongo

        :return:
        the connector
        '''
        if conn_type not in ConnectorFactory.connectors:
            return None
        else:
            if conn_type == 'E':
                return ElasticConnection()
            elif conn_type == 'M':
                return MongoConnection()


if __name__ == '__main__':
    '''
    Getting time from different mongo operations

    :args:
    operation - 0 all, 1 count, 2 to, 3 word
    system - E: elasticSearch, M: mongoDB
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

    parser.add_argument('--system',
                        '-s',
                        dest='system',
                        default='E',
                        choices=['M', 'E'],
                        help='"M": mongo, "E": elastic or "B": both(default)',
                        required=False)

    args = parser.parse_args()

    # getting mongo connector
    conn = ConnectorFactory.create_connector(args.system)

    if args.system == 'E':
        conn_name = 'ElastisSearch'
    else:
        conn_name = 'MongoDB'

    if args.op == 0 or args.op == 1:
        # count
        time1 = datetime.now()
        total = conn.count_all()
        time2 = datetime.now()
        result = time2 - time1
        print "%s query time (microseconds): %f" % (conn_name, result.microseconds)
        print "%s count: %s" % (conn_name, total)

    elif args.op == 0 or args.op == 2:
        # getting docs with a mail in 'to' list
        to_user = 'steven.kean@enron.com'
        time1 = datetime.now()
        tos = conn.get_to_user(to_user)
        time2 = datetime.now()
        result = time2 - time1
        print "%s query time (microseconds): %f" % (conn_name, result.microseconds)
        conn.print_result('get_to_user', tos, num=1)

    if args.op == 0 or args.op == 3:
        # getting docs with a word in body
        word_body = 'humongous'
        time1 = datetime.now()
        bodies = conn.get_word_in_body(word_body)
        conn.print_result('get_word_in_body', bodies, num=1)
        time2 = datetime.now()
        result = time2 - time1
        print "%s query time (microseconds): %f" % (conn_name, result.microseconds)

    if args.op == 0 or args.op == 4:
        # getting docs with a word in body (complex)
        word_body = 'Compass'
        time1 = datetime.now()
        bodies = conn.get_word_in_body_complex(word_body, NUM_RESULTS)
        time2 = datetime.now()
        result = time2 - time1
        print "ElastisSearch complex query time (microseconds): %f" % (result.microseconds)
        print "%s query time (microseconds): %f" % (conn_name, result.microseconds)
        conn.print_result('get_word_in_body_complex', bodies, NUM_RESULTS)
