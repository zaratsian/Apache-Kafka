<h3>Apache Kafka</h3>
<br>Start:
<br>```nohup ./bin/zookeeper-server-start.sh config/zookeeper.properties > /dev/null 2>&1 &```
<br>```nohup ./bin/kafka-server-start.sh config/server.properties > /dev/null 2>&1 &```
<br>
<br>Create Topic:
<br>```./bin/kafka-topics.sh --create --zookeeper zkhost:2181 --replication-factor 1 --partitions 1 --topic topicdz1```
<br>
<br>List Topics:
<br>```./bin/kafka-topics.sh --zookeeper zkhost:2181 --list```
<br>
<br>CMD Line Producer:
<br>```echo "DZ Test Message" | ./bin/kafka-console-producer.sh --broker-list kafkahost:6667 --topic topicdz1 > /dev/null```
<br>
<br>CMD Line Consumer:
<br>```./bin/kafka-console-consumer.sh --zookeeper zkhost:2181 --topic topicdz1 --from-beginning```
<br>
<br><b>References:</b>
<br><a href="https://kafka.apache.org/documentation/">Kafka Documentation</a>
<br><a href="https://pypi.python.org/pypi/pykafka/2.6.0.dev2">PyKafka</a>
