
#####################################################################
#
#   Data Simulator for Apache Kafka
#
#   USAGE:
#   simulate_to_kafka.py --bootstrap_servers localhost:9092 --kafka_topic dztopic1 --time_delay 1 --send_to_kafka 0
#
#   Test with python 3.7
#   https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
#
#   Prereqs:
#   pip install kafka-python
#
#####################################################################
'''
./params.py

bootstrap_servers   = 'kafka-instance-1-vm:9092'
send_to_kafka       = 0
kafka_topic         = 'eye_tracking'
time_delay          = 1
number_of_threads   = 5

'''

from kafka import KafkaProducer
import json
import re
import datetime, time
import random
import argparse
import threading
import params



def simulate_payload():
    
    datetimestamp = datetime.datetime.now()
    
    payload = {
        'id':           datetimestamp.strftime('%Y%m%d%H%M%S%f'),
        'datetimestamp':datetimestamp.strftime('%Y-%m-%d %H:%M:%S.%f'),
        'heart_rate':   int(random.triangular(35,70,175))
    }
    
    return payload



def initialize_kafka_producer(params):
    try:
        producer = KafkaProducer(bootstrap_servers=params.bootstrap_servers, value_serializer=lambda v: json.dumps(v).encode('utf-8'))     # JSON-based Producer
    except Exception as e:
        print('[ EXCEPTION ] Could not connect to Kafka bootstrap server - {}'.format(e))
    
    return producer



def publish_kafka_event(params, producer, counter):
    
    while True:
        
        payload = simulate_payload()
        payload['counter'] = counter
        
        if params.send_to_kafka==1:
            try:
                producer.send(params.kafka_topic, value=payload)   # JSON-based kafka commit
            except Exception as e:
                print('[ EXCEPTION ] Failure sending JSON payload to Kafka producer - {}'.format(e))
        else:
            print('{}\n'.format(payload))
        
        time.sleep(params.time_delay)



if __name__ == "__main__":
    
    producer = initialize_kafka_producer(params)
    
    threads = []
    for i in range(params.number_of_threads):
        threads.append(threading.Thread(target=publish_kafka_event, args=(params, producer, i,)))
    
    for thread in threads:
        thread.start()



#ZEND
