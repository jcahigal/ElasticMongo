'''
Created on 01/03/2016

@author: juanc352 (jchernandez@full-on-net.com)
'''
from __future__ import unicode_literals
import abc


class Connector(object):
    '''
    Class with all required method for any connector to test.
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_connector(self):
        '''
        Function to create a mongoDB connector to one DB.

        :return:
            db connector
        '''
        raise NotImplementedError

    @abc.abstractmethod
    def count_all(self):
        '''
        Return the count of docs in mongoDB (op 1).

        :return:
            count of all documents
        '''
        raise NotImplementedError

    @abc.abstractmethod
    def get_to_user(self, user):
        '''
        Get all documents with a particular header To (op 2).

        :args:
            user name of the user

        :return:
            JSON with resulting entries
        '''
        raise NotImplementedError

    @abc.abstractmethod
    def get_word_in_body(self, word):
        '''
        Get all documents with a particular word in its body (op 3).

        :args:
            word word to find in body

        :return:
            Mongo bodies resulting documents
        '''
        raise NotImplementedError

    @abc.abstractmethod
    def get_word_in_body_complex(self, word, num_results):
        '''
        Get all documents with a particular word in its body (op 4).

        :args:
            word word - to find in body
            num_results - number of results to return

        :return:
            Mongo bodies resulting documents
        '''
        raise NotImplementedError

    @abc.abstractmethod
    def print_result(self, res, num=0):
        '''
        print result for this connector

        :args:
            res - query results
            num - number of results to print
        '''
        raise NotImplementedError
