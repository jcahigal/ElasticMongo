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

from conn.connector import Connector

# Elastic result fields
ELASTIC_HITS_LABEL = 'hits'
ELASTIC_TOTAL_LABEL = 'total'

ELASTIC_SUGGEST_REQUEST = "demo-suggestion"

ASC_ORDER = "asc"
NUM_RESULTS = 2


class ElasticConnection(Connector):
    '''
    Class to manage the connector with ElasticSearch
    '''
    # equivalent to DB
    ES_INDEX = "demo"

    # equivalent to collection
    ES_DOC_TYPE = "elastic"

    es = None

    @staticmethod
    def get_connector():
        '''
        Function to create a mongoDB connector to one DB.

        :return:
            db connector
        '''
        if not ElasticConnection.es:
            print 'creating elastic connector'
            ElasticConnection.es = Elasticsearch()

        return ElasticConnection.es

    def get_all(self):
        '''
        Return all docs in Elastic.

        :return:
            ES search with all documents
        '''
        es_con = ElasticConnection.get_connector()
        return es_con.get(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE)

    def count_all(self):
        '''
        Return the count of docs in Elastic (op 1).

        :return:
            count of all documents
        '''
        es_con = ElasticConnection.get_connector()
        return es_con.count(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE)

    def get_to_user(self, user):
        '''
        Get all documents with a particular header To (op 2).

        :args:
            user name of the user

        :return:
            ES resulting documents
        '''

        """
        example of the same query with Lucence syntax

        query_to = 'headers.To:%s' %(user)
        result = es_con.search(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE, q=query_to)
        """
        query_to = {
            "query": {
                "match": {
                    ElasticMongo.ELASTIC_TYPE_TO: user
                }
            }
        }

        es_con = ElasticConnection.get_connector()
        result = es_con.search(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE, body=query_to)
        return result

    def get_word_in_body(self, word):
        '''
        Get all documents with a particular word in its body (op 3).

        :args:
            word word to find in body

        :return:
            ES resulting documents (only body in source)
        '''

        query_to = {
                "query": {
                    "match": {
                        ElasticMongo.ELASTIC_TYPE_BODY: word
                    }
                },
                "fields": [ElasticMongo.ELASTIC_TYPE_BODY]
            }

        es_con = ElasticConnection.get_connector()
        result = es_con.search(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE, body=query_to)
        return result

    def get_word_in_body_complex(self, word, num_results):
        '''
        Get all documents with a particular word in its body (op 4).

        :args:
            word word - to find in body
            num_results - number of results to return

        :return:
            ES resulting documents (only body in source)
        '''

        query_to = {
                "query": {
                    "match": {
                        ElasticMongo.ELASTIC_TYPE_BODY: word
                    }
                },
                "fields": [ElasticMongo.ELASTIC_TYPE_SUBJECT, ElasticMongo.CREATION_LABEL]
            }

        sort_request = "%s:%s" % (ElasticMongo.CREATION_LABEL, ASC_ORDER)

        es_con = ElasticConnection.get_connector()

        result = es_con.search(index=ElasticConnection.ES_INDEX,
                               doc_type=ElasticConnection.ES_DOC_TYPE,
                               body=query_to,
                               sort=sort_request,
                               size=num_results)
        return result

    def get_suggestion(self, text):
        '''
        Suggest similar looking terms based on a provided text(op 5).

        :args:
            text text for suggestion

        :return:
            ES resulting suggestions
        '''

        suggest = {
                  ELASTIC_SUGGEST_REQUEST: {
                    "text": text,
                    "term": {
                      "field": ElasticMongo.ELASTIC_TYPE_BODY
                    }
                  }
                }
        es_con = ElasticConnection.get_connector()
        result = es_con.suggest(index=ElasticConnection.ES_INDEX, body=suggest)
        return result

    def print_result(self, query, res, num=0):
        '''
        print result for elastic connector

        :args:
            query - name
            res - query results
            num - number of results to print
        '''
        if res:
            total = res[ELASTIC_HITS_LABEL][ELASTIC_TOTAL_LABEL]
            print "Collections in ES for %s has had %s results." % (query, total)

            if num == 0:
                num_iter = total - 1
            else:
                if num >= total:
                    num_iter = total - 1
                else:
                    num_iter = num

            for i in range(0, num_iter):
                print res[ELASTIC_HITS_LABEL][ELASTIC_HITS_LABEL][i]


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
                        '-op',
                        dest='op',
                        type=int,
                        help='index of the operation to run, 0 to all',
                        required=True)
    args = parser.parse_args()

    # getting ElastisSearch connector
    es = ElasticConnection()

    if args.op == 0 or args.op == 5:
        # getting suggestions for words in a text
        text = "El desarroyo de MangoDB"
        time1 = datetime.now()
        suggestions = es.get_suggestion(text)
        time2 = datetime.now()
        result = time2 - time1
        print "ElastisSearch suggest time (microseconds): %f" % (result.microseconds)
        print "Suggestions in ES for %s in its body" % (text)
        for suggest in suggestions[ELASTIC_SUGGEST_REQUEST]:
            print suggest
