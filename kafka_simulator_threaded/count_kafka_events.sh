

/opt/kafka/bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic eye_tracking


# /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic eye_tracking --from-beginning | grep "2019-01-23 02:50" > /tmp/kafka_count.txt
# cat /tmp/kafka_count.txt | wc -l


#ZEND
