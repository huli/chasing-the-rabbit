#!/usr/bin/env python

import pika

# Connecting to a local broker
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=5672))
channel = connection.channel()

# Create a queue
channel.queue_declare(queue='hello')

# Now sending a message over the default exhange
channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello World!')
print(" [x] sent 'Hello World!'")

# Make shure network buffers are flushed and our message is delivered
connection.close()


