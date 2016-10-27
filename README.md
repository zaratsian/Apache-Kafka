<h3>Apache Kafka</h3>
<br><b>Command line Tools</b>
<br>
<br>Create Topic:
<br>```./bin/kafka-topics.sh --create --zookeeper zkhost:2181 --replication-factor 1 --partitions 1 --topic topicdz1```
<br>
<br>List Topics:
<br>```./bin/kafka-topics --zookeeper zkhost:2181 --list```
<br>
<br>CMD Line Producer:
<br>```echo "DZ Test Message" | ./bin/kafka-console-producer.sh --broker-list zkhost:6667 --topic topicdz1 > /dev/null```
<br>
<br>CMD Line Consumer:
<br>```./bin/kafka-console-consumer.sh --zookeeper zkhost:2181 --topic topicdz1 --from-beginning```
<br>
<br>References:
<br>
