'''
Created on 25/04/2016

Module to load the data in ES from TU project.

Run with:
>python utils\load_TU_data.py -f "rgConnectOBsFTH_c700.log"


ElasticSearch
--------------
* index 'tu', type 'gob'
* drop index with: curl -X DELETE "http://localhost:9200/tu/"

@author: juanc352 (jchernandez@full-on-net.com)
'''

from __future__ import unicode_literals
from es.elastic_search import ElasticConnection
from datetime import datetime
# from datetime import timedelta

import argparse

ES_TU_INDEX = "tu"
ES_TU_TYPE = "gob"

LOG_FILE_PREFFIX = 'rgConnectOBs'
LOG_FILE_SUFFIX = '_'
LOG_LINE_SEPARATOR = ' '
LOG_STATUS_LINE = 'STATUS'

CORR_INFO_ORIGINATOR = "originator"
CORR_INFO_TOKEN = "unique_token"
CORR_INFO_FLOW_ID = "flow_id"
CORR_INFO_SAMPLER = "sampler"
CORR_INFO_USER = "user"

CORR_OLD_VALUE = "value"
CORR_OLD_OB = "OB"
CORR_OLD_OB_LOC = "location"


def get_module_name(file_name):
    '''
    Extract the module name from the log file name.

    :args:
        file_name - log file name

    :return:
        module name
    '''
    if file_name and len(file_name) > 0:
        index_name = file_name.index(LOG_FILE_PREFFIX)
        if index_name > 0:
            index_name = index_name + len(LOG_FILE_PREFFIX)
            return file_name[index_name:file_name.index(LOG_FILE_SUFFIX)]
        else:
            raise KeyError('Wrong log file name')
    else:
        raise KeyError('Wrong log file name')


def process_new_correlator(correlator):
    '''
    Divide information from the new correlator.

    :args:
        correlator

    :return:
        correlator info - dictionary with fields originator, unique_token, flow_id, sampler and user
    '''
    try:
        correlator_info = {}
        last_correlator = "."

        # originator: node ID
        last_index = correlator.index(last_correlator)
        correlator_info[CORR_INFO_ORIGINATOR] = correlator[:last_index]

        # unique_token
        last_index = last_index + len(last_correlator)
        new_index = correlator.index(last_correlator, last_index)
        correlator_info[CORR_INFO_TOKEN] = correlator[last_index:new_index]

        # flow_id: CT, VO, ST, SO, VT
        last_index = new_index + len(last_correlator)
        last_correlator = "#"
        new_index = correlator.index(last_correlator, last_index)
        correlator_info[CORR_INFO_FLOW_ID] = correlator[last_index:new_index]

        # Sampler
        last_index = new_index + len(last_correlator)
        last_correlator = ":"
        new_index = correlator.index(last_correlator, last_index)
        correlator_info[CORR_INFO_SAMPLER] = correlator[last_index:new_index]

        # user
        last_index = new_index + len(last_correlator)
        correlator_info[CORR_INFO_USER] = correlator[last_index:]
        return correlator_info
    except:
        return None


def set_OB_location(ob_code):
    '''
    Get the geopoint of the capital of the country.
    refs.:
        http://www.numberportabilitylookup.com/networks?s=
        http://dateandtime.info/es/citycoordinates.php?id=3936456

    :args:
        ob_code

    :return:
        geopoint in string format: "lan, lon"
    '''
    if "72406" == ob_code or "72410" == ob_code or "72411" == ob_code or "72423" == ob_code:
        # Brazil
        return "-15.779, -47.929"

    elif "23402" == ob_code or "23410" == ob_code or "23411" == ob_code:
        # United Kingdom
        return "51.508, -0.125"

    elif "732103" == ob_code or "732111" == ob_code or "732123" == ob_code:
        # Colombia
        return "4.609, -74.081"

    elif "72270" == ob_code:
        # Argentina
        return "-34.613, -58.377"

    elif "71606" == ob_code:
        # Peru
        return "-12.043, -77.028"

    elif "33403" == ob_code:
        # Mexico
        return "19.428, -99.127"


def process_old_correlator(correlator):
    '''
    Divide information from the old correlator.

    :args:
        correlator

    :return:
        correlator info - dictionary with fields value, ob
    '''
    try:
        # value
        correlator_info = {CORR_OLD_VALUE: correlator}
        fragments_info = correlator.split("-")

        # OB
        correlator_info[CORR_OLD_OB] = fragments_info[-1]

        # OB capital geo location
        correlator_info[CORR_OLD_OB_LOC] = set_OB_location(fragments_info[-1])
        return correlator_info
    except:
        return None


def extract_log_line_info(line):
    '''
    Extract the information from every log line.

    :args:
        line - full line

    :return:
        info - tuple with (date, request_id, old_correlator, new_correlator, algo, time, tick_type, tick_code)
    '''
    if line and len(line) > 0:
        try:
            line.index(LOG_STATUS_LINE)
            return None
        except:
            # not status line
            try:
                this_year = str(datetime.now().year)
                fields = line.split(LOG_LINE_SEPARATOR)
                request_date = "%s-%s-%s %s" % (this_year, fields[0][:2], fields[0][2:], fields[1])

                ids = fields[7]
                request_id = ids[1:ids.index(']')]
                old_correlator = ids[ids.index('[', 1) + 1:-1]
                old_correlator_processed = process_old_correlator(old_correlator)

                new_correlator = fields[8][1:-1]
                new_correlator_processed = process_new_correlator(new_correlator)

                # ignore us and convert to ms
                request_timestamp = float(fields[9][1:]) / 1000000
                request_timestamp = datetime.fromtimestamp(request_timestamp)

                time = fields[11][1:]

                tick_type = fields[13]

                tick_code = fields[14][:-1]
                return (request_date,
                        request_id,
                        old_correlator_processed,
                        new_correlator_processed,
                        request_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                        time,
                        tick_type,
                        tick_code)
            except:
                # not a gOB generated log
                return None


if __name__ == '__main__':

    # reading args
    parser = argparse.ArgumentParser(description='loader of TU logs')
    parser.add_argument('--file',
                        '-f',
                        dest='log_file',
                        help='path and name to log file',
                        required=True)

    args = parser.parse_args()

    module = get_module_name(args.log_file)

    es = ElasticConnection.get_connector()

    # inserting
    time1 = datetime.now()
    with open(args.log_file) as f:
        content = f.readlines()
        for log in content:
            line_info = extract_log_line_info(log)
            if line_info:
                new_entry = {
                            'module': module,
                            'date': line_info[0],
                            'request_id': line_info[1],
                            'old_correlator': line_info[2],
                            'new_correlator': line_info[3],
                            'request_timestamp': line_info[4],
                            'time': line_info[5],
                            'tick_type': line_info[6],
                            'tick_code': line_info[7]
                            }
                print new_entry
                es.index(index=ES_TU_INDEX, doc_type=ES_TU_TYPE, body=new_entry)

    time2 = datetime.now()
    result = time2 - time1
    print "insert time (microseconds): %f" % (result.microseconds)
