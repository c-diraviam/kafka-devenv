#!/usr/local/bin/python3

from kafka import KafkaConsumer

'''Python kafka consumer sample implementation''' 


kafka_consumer=KafkaConsumer('kafka_test', bootstrap_servers=['kafka:9092'])
for msg in kafka_consumer:
    print(msg)