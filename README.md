<h3>Apache Kafka</h3>
<br><b>Start:</b>
<br>nohup ./bin/zookeeper-server-start.sh config/zookeeper.properties > /dev/null 2>&1 &
<br>nohup ./bin/kafka-server-start.sh config/server.properties > /dev/null 2>&1 &    # Kafka Broker 1
<br>nohup ./bin/kafka-server-start.sh config/server2.properties > /dev/null 2>&1 &   # Kafka Broker 2
<br>nohup ./bin/kafka-server-start.sh config/server3.properties > /dev/null 2>&1 &   # Kafka Broker 3
<br>
<br><b>Create Topic:</b>
<br>./bin/kafka-topics.sh --create --zookeeper zkhost:2181 --replication-factor 1 --partitions 1 --topic dztopic1
<br>
<br><b>Delete Topic:</b>
<br>./bin/kafka-topics.sh --delete --zookeeper localhost:2181 --topic dztopic1
<br>
<br><b>List Topics:</b>
<br>./bin/kafka-topics.sh --zookeeper zkhost:2181 --list
<br>
<br><b>Describe Topic:</b>
<br>./bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic dztopic1
<br>
<br><b>CMD Line Producer:</b>  (Default Broker Port: 9092, Hortonworks uses broker port: 6667)
<br>echo "DZ Kafka Event at $(date)" | ./bin/kafka-console-producer.sh --broker-list kafkahost:9092 --topic dztopic1 > /dev/null
<br>
<br><b>CMD Line Consumer:</b> (Default Broker Port: 9092, Hortonworks uses broker port: 6667)
<br>./bin/kafka-console-consumer.sh --bootstrap-server kafka_broker:6667 --topic dztopic1 --from-beginning
<br>
<br><b>References:</b>
<br><a href="https://kafka.apache.org/documentation/">Kafka Documentation</a>
<br><a href="https://pypi.python.org/pypi/pykafka/2.6.0.dev2">Python PyKafka</a>
<br><a href="https://pypi.python.org/pypi/kafka/1.2.5">Python Kafka</a>
