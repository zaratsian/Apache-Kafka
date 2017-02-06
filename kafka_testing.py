

#################################################################
#
#   Consumer
#
#################################################################

import datetime,re

#---------------------------
#  Python Only (prints) 
#---------------------------

iterations_per_second = []

for iteration in range(5):
    next_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
    end_time  = next_time + datetime.timedelta(seconds=1)
    
    i = 0
    while datetime.datetime.now() <= end_time:
        if (next_time <= datetime.datetime.now() <= end_time):
            i += 1
            print str(i)
    
    iterations_per_second.append(i)

print '\n\nAverage writes per second: ' + str(sum(iterations_per_second) / float(5)) + '\n\n'
# Average writes per second: 20889.2



#---------------------------
#  Python - pykafka
#---------------------------

import datetime, re
from pykafka import KafkaClient

client = KafkaClient(hosts="kafka.dev:9092")

client.topics

topic = client.topics['dztopic1']

iterations_per_second = []

for iteration in range(5):
    next_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
    end_time  = next_time + datetime.timedelta(seconds=1)
    
    i = 0
    with topic.get_sync_producer() as producer:
        while datetime.datetime.now() <= end_time:
            if (next_time <= datetime.datetime.now() <= end_time):
                i += 1
                producer.produce('test message ' + str(i))
    
    iterations_per_second.append(i)

print '\n\nAverage writes per second: ' + str(sum(iterations_per_second) / float(5)) + '\n\n'
# Average writes per second: 106.2



#---------------------------
#  Python - kafka
#---------------------------

import datetime,re
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka.dev:9092')

iterations_per_second = []

for iteration in range(5):
    next_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
    end_time  = next_time + datetime.timedelta(seconds=1)
    
    i = 0
    while datetime.datetime.now() <= end_time:
        if (next_time <= datetime.datetime.now() <= end_time):
            i += 1
            producer.send('dztopic1', 'test message ' + str(i))
    
    iterations_per_second.append(i)

print '\n\nAverage writes per second: ' + str(sum(iterations_per_second) / float(5)) + '\n\n'
# Average writes per second: 1683.6



#################################################################
#
#   Producer
#
#################################################################

#---------------------------
#  Python - pykafka
#---------------------------

import datetime,re
from pykafka import KafkaClient

client = KafkaClient(hosts="kafka.dev:9092")

client.topics

topic = client.topics['dztopic1']

consumer = topic.get_simple_consumer()

for message in consumer:
     if message is not None:
         print message.offset, message.value



#---------------------------
#  Python - kafka
#---------------------------

from kafka import KafkaConsumer

consumer = KafkaConsumer('dztopic1')

for msg in consumer:
    print str(msg)




#ZEND
