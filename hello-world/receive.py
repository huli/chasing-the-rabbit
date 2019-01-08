#!/usr/bin/env python

import pika

# Connecting to a local broker
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=5672))
channel = connection.channel()

# Create a queue
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()