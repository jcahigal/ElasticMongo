# -*- encoding: utf-8 -*-
'''
Created on 08/01/2016

@author: juanc352 (jchernandez@full-on-net.com)
'''

from __future__ import unicode_literals
from datetime import datetime
from elasticsearch import Elasticsearch
from utils.resources import ElasticMongo
import random
import argparse


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
            print 'creating es'
            ElasticConnection.es = Elasticsearch()

        return ElasticConnection.es

if __name__ == '__main__':
    '''
    Getting time from a simple query of all elements in Elastic.
    '''
    es = ElasticConnection.get_elastic_connector()
    time1 = datetime.now()
    es.get(index=ElasticConnection.ES_INDEX, doc_type=ElasticConnection.ES_DOC_TYPE)
    time2 = datetime.now()
    result = time2 - time1
    print "ElastisSearch query time (microseconds): %f" % (result.microseconds)
