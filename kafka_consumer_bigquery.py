
#####################################################################
#
#   Kafka Consumer - Stream data to Google BigQuery
#
#   USAGE: python kafka_consumer_bigquery.py &
#
#   Requirements:
#       pip install kafka-python
#       pip install --upgrade google-cloud-bigquery
#
#####################################################################

import os
import threading, logging, time
import multiprocessing
import json
from kafka import KafkaConsumer, KafkaProducer
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/xyz/key.json"  # Service Acct

#####################################################################
#
#   Functions
#
#####################################################################

def bg_streaming_insert(rows_to_insert, bq_dataset_id, bq_table_id):
    ''' BigQuery Streaming Insert - Insert python list into BQ '''
    
    # Note: The table must already exist and have a defined schema
    # rows_to_insert is a list of variables (i.e. (id, date, value1, value2, etc.))
    #print('[ INFO ] Inserting records in BigQuery')
    client    = bigquery.Client()
    table_ref = client.dataset(bq_dataset_id).table(bq_table_id)
    table     = client.get_table(table_ref)
    errors    = client.insert_rows(table, rows_to_insert)
    if errors == []:
        print('[ Success ] Streaming Insert into BigQuery Complete')
    else:
        print('[ WARNING ] Issue inserting into BigQuery')


def kafka_consumer_to_bigquery():
    
    stop_event = multiprocessing.Event()
    
    # https://kafka-python.readthedocs.io/en/master/apidoc/kafka.html#kafka.KafkaConsumer
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, auto_offset_reset='latest', consumer_timeout_ms=1000)
    
    consumer.subscribe([kafka_topic])
    
    while not stop_event.is_set():
        for message in consumer:
            #print(message)
            rows_to_insert = [json.loads(message.value)]
            bg_streaming_insert(rows_to_insert, bq_dataset_id, bq_table_id)
            if stop_event.is_set():
                break
    
    consumer.close()


#####################################################################
#
#   Main
#
#####################################################################

if __name__ == "__main__":
    
    kafka_topic         = ''
    bootstrap_servers   = 'localhost:9092'
    bq_dataset_id       = ''
    bq_table_id         = ''
    
    kafka_consumer_to_bigquery()



#ZEND
