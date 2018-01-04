#!/usr/local/bin/python
from kafka import KafkaProducer

kafka_producer=KafkaProducer(bootstrap_servers='kafka:9092')
'''
for value in range(100):
    sent_data=kafka_producer.send('kafka_test', b'msg: %d' %value)
    test_data=sent_data.get(timeout=60)
    '''
input_file=open('./readfile','r')
#content=input_file.readlines()
#print(content)
for char in input_file:
    print(len(char))
    kafka_producer.send('kafka_test', b'msg_size: %d' %len(char))

'''
content=input_file.readlines()
print(content)
kafka_producer.send('kafka_test', b'msg: %s' %content)'''