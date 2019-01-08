#!/usr/bin/env python

import pika

# Connecting to a local broker
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=5672))
channel = connection.channel()

# Create a queue
channel.queue_declare(queue='task_queue', durable=True)

import time

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

# Allow only one message to be prefetched
channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                      queue='task_queue',
                      no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

