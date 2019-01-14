
#####################################################################
#
#   Data Simulator for Apache Kafka
#
#   USAGE:
#   simulate_to_kafka.py --kafka_topic dztopic1 --time_delay 1 --send_to_kafka False
#
#   Test with python 3.7
#   https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
#
#   Prereqs:
#   pip install kafka-python
#
#####################################################################

from kafka import KafkaProducer     
import json
import re
import datetime, time
import random
import argparse



def simulate_payload():
    
    datetimestamp = datetime.datetime.now()
    pupil_x_angle = random.randint(-90,90)
    pupil_y_angle = random.randint(-90,90)
    pupil_size    = round(random.triangular(1,3,9),2)
    
    payload = {
        'id':           datetimestamp.strftime('%Y%m%d%H%M%S%f'),
        'date':         datetimestamp.strftime('%Y-%m-%d'),
        'timestamp':    datetimestamp.strftime('%H:%M:%S.%f'),
        'leye_x_angle': pupil_x_angle,
        'leye_y_angle': pupil_y_angle,
        'leye_size_mm': pupil_size,
        'reye_x_angle': pupil_x_angle if random.random()<=0.95 else random.randint(-90,90),
        'reye_y_angle': pupil_y_angle if random.random()<=0.95 else random.randint(-90,90),
        'reye_size_mm': pupil_size if random.random()<=0.95 else random.triangular(1,3,9),
        'heart_rate':   int(random.triangular(35,70,175)),
        'blink':        random.randint(0,1)
    }
    
    return payload



if __name__ == "__main__":
    
    # ONLY used for TESTING - Example Arguments
    #args =  {
    #           "kafka_topic":   "dztopic1",
    #           "time_delay":    1,
    #           "send_to_kafka": False,
    #       }
    
    # Arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("--kafka_topic",    required=True,                                help="Apache Kafka Topic Name")
    ap.add_argument("--time_delay",     required=False, default=1,     type=int,      help="Time delay inbetween simulations (seconds)")
    ap.add_argument("--send_to_kafka",  required=False, default=False, type=str2bool, help="Send to Kafka (True) or send to console (False)")
    args = vars(ap.parse_args())
    
    try:
        # Setup Kafka Producer
        #producer= KafkaProducer(bootstrap_servers=['localhost:9092'])                          # String-based Producer
        producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))      # JSON-based Producer
    except Exception as e:
        print('[ EXCEPTION ] {}'.format(e))
    
    counter = 0
    while True:
        
        counter += 1
        
        payload = simulate_payload()
        
        if send_to_kafka:
            #producer.send(kafka_topic, 'test message {}'.format(counter).encode('utf-8') )     # String-based kafka commit
            producer.send(kafka_topic, value=payload)                                           # JSON-based kafka commit
        else:
            print(payload)
            print('\n')
        
        time.sleep(time_delay)



#ZEND
