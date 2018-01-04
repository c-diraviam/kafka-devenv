#!/usr/bin/env python3
from kafka import KafkaProducer
from kafka.errors import KafkaError

kafka_producer=KafkaProducer(bootstrap_servers='kafka:9092')

input_file=open('/code/sample/readfile','r')

for char in input_file:
    #print(char)
    byte_str=str.encode(char)
    #kafka_producer.send('kafka_test', b'msg_size: %d' %len(char))
    
    future=kafka_producer.send('kafka_test', b"%b" %byte_str)

    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        pass
