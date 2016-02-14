# -*- encoding: utf-8 -*-
'''
Created on 08/01/2016

@author: juanc352 (jchernandez@full-on-net.com)
'''

from __future__ import unicode_literals
from datetime import datetime
from elasticsearch import Elasticsearch
from utils.resources import ElasticMongo
import argparse

ELASTIC_HITS_LABEL = 'hits'
ELASTIC_TOTAL_LABEL = 'total'


class ElasticConnection(object):
    '''
    Class to manage the connector with ElasticSearch
    '''
    # equivalent to DB
    ES_INDEX = "demo"

    # equivalent to collection
    ES_DOC_TYPE = "elastic"

    es = None

    @staticmethod
    def get_elastic_connector():
        '''
        Function to create a mongoDB connector to one DB.

        :return:
            db connector
        '''
        if not ElasticConnection.es:
            print 'creating elastic connector'
            ElasticConnection.es = Elasticsearch()

        return ElasticConnection.es

    @staticmethod
    def get_all(es_con):
        '''
        Return all docs in Elastic.

        :args:
            es_con ElastisSearch connector

        :return:
            ES search with all documents
        '''
        return es_con.get(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE)

    @staticmethod
    def count_all(es_con):
        '''
        Return the count of docs in Elastic.

        :args:
            es_con ElastisSearch connector

        :return:
            count of all documents
        '''
        return es_con.count(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE)

    @staticmethod
    def get_to_user(es_con, user):
        '''
        Get all documents with a particular header To.

        :args:
            es_con ElastisSearch connector
            user name of the user

        :return:
            ES resulting documents
        '''

        """
        example of the same query with Lucence syntax

        query_to = 'headers.To:%s' %(user)
        result = es_con.search(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE, q=query_to)
        """
        query_to0 = {
            "query": {
                "match": {
                    "headers.To": user
                }
            }
        }
        
        query_to = {
                    "query": {
                        "filtered": {
                            'filter': {
                                "bool": {
                                    "must": [{
                                            "term": {
                                                "headers.To": user
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }

        result = es_con.search(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE, body=query_to)
        return result

    @staticmethod
    def get_word_in_body(es_con, word):
        '''
        Get all documents with a particular word in its body.

        :args:
            es_con ElastisSearch connector
            word word to find in body

        :return:
            ES resulting documents
        '''

        query_to = {
                        "query": {
                            "match": {
                                "body": word
                            }
                        }
                    }

        """
                    "query_hint": word,
                    "field_mapping": {
                        "title": [
                            "_source.headers.Subject"
                        ],
                        "content": [
                            "_source.body"
                        ]
                    }
           """

        result = es_con.search(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE, body=query_to)
        return result

    '''
    {
  "query": {
    "match_phrase_prefix": {
      "descripcion_gim": {
        "query": "impresora",
        "slop": 2,
        "max_expansions": 5
      }
    }
  }
    }
    '''

if __name__ == '__main__':
    '''
    Getting time from different Elastic operations.

    :args:
    operation: 0 all, 1 count, 2 to, 3 word
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

    # getting ElastisSearch connector
    es = ElasticConnection.get_elastic_connector()

    if args.op == 0 or args.op == 1:
        # count all
        time1 = datetime.now()
        total = ElasticConnection.count_all(es)
        time2 = datetime.now()
        result = time2 - time1
        print "ElastisSearch query time (microseconds): %f" % (result.microseconds)
        print "ElastisSearch count: %s" % (total)

    if args.op == 0 or args.op == 2:
        # getting docs with a mail in 'to' list
        to_user = 'steven.kean@enron.com'
        time1 = datetime.now()
        tos = ElasticConnection.get_to_user(es, to_user)
        time2 = datetime.now()
        result = time2 - time1
        print "ElastisSearch query time (microseconds): %f" % (result.microseconds)
        print "collections in ES with %s header to %s" % (to_user, tos[ELASTIC_HITS_LABEL][ELASTIC_TOTAL_LABEL])
        for to in tos[ELASTIC_HITS_LABEL][ELASTIC_HITS_LABEL]:
            print to

    if args.op == 0 or args.op == 3:
        # getting docs with a word in body
        word_body = 'humongous'
        time1 = datetime.now()
        bodies = ElasticConnection.get_word_in_body(es, word_body)
        time2 = datetime.now()
        result = time2 - time1
        print "ElastisSearch query time (microseconds): %f" % (result.microseconds)
        print "collections in ES with %s word in its body %s" % (word_body, bodies[ELASTIC_HITS_LABEL][ELASTIC_TOTAL_LABEL])
        for body in bodies[ELASTIC_HITS_LABEL][ELASTIC_HITS_LABEL]:
            print body

