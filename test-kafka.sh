#!/usr/bin/env bash

# start the docker services 

docker-compose -f docker-compose.yml up -d 

# Scale kafka to multi node
docker-compose scale kafka=4

# Create kafka topic

docker-compose exec kafka bash -c "/opt/kafka/bin/kafka-topics.sh --zookeeper zookeeper:2181 --create --topic kafka_topic --replication-factor 3 --partitions=2"

# Test if the topic has been created

if `docker-compose exec kafka bash -c "bin/kafka-topics.sh --zookeeper zookeeper:2181 --list | grep -q kafka_topic "`
then
    echo "kafka_topic created"
else
    echo "Kafka topic creation failed"
    exit 1
fi

# Start python-consumer in background
echo "Reading from kafka"
docker-compose exec python-kafka python /code/sample/python-consumer.py 


echo " Now you could run the following and see printed in console"
echo
echo
echo "docker-compose exec python-kafka python /code/sample/python-producer.py"




 


