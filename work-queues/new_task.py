#!/usr/bin/env python

import pika
import sys

# Connecting to a local broker
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=5672))
channel = connection.channel()

# Create a queue
channel.queue_declare(queue='task_queue', durable=True)


message = ' '.join(sys.argv[1:]) or "Hello World!"

# Publish message
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2, # persistent
                      ))
print(" [x] Sent %r" % message)


