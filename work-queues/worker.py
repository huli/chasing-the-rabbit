#!/usr/bin/env python

import pika

# Connecting to a local broker
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=5672))
channel = connection.channel()

# Create a queue
channel.queue_declare(queue='hello', durable=True)

import time

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

