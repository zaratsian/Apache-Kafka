FROM python:3.7.2-alpine3.7

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

#EXPOSE 80

CMD ["python", "app.py", "--bootstrap_servers", "kafka-instance-1-vm:9092", "--kafka_topic", "eye_tracking", "--time_delay", "1", "--send_to_kafka", "1"]

#ZEND
