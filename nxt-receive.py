#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('craig', 'craig')
parameters=pika.ConnectionParameters('10.238.131.199',
                                           5672,
                                          'arrisSales',
                                          credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='nxt-eng-in',
                         exchange_type='tenant-out',
                         durable=True )

result = channel.queue_declare(durable=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s  [binding_key]\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='nxt-eng-in',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for NXT messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

