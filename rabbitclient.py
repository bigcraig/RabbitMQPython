#!/usr/bin/env python
import pika
import sys
import base64
import zlib
import gzip

import StringIO
import json
credentials = pika.PlainCredentials('craig', 'craig')
parameters=pika.ConnectionParameters('10.238.131.199',
                                           5672,
                                          'arrisSales',
                                          credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='tenant-out',
                         exchange_type='topic',
                         durable=True )




print(' [*] Waiting for NXT messages. To exit press CTRL+C')

def callback(ch, method, properties, body):

      decoded_data=gzip.GzipFile(fileobj=StringIO.StringIO(body)).read()
      print(" Routing Key %r" % (method.routing_key))
      parsed = json.loads(decoded_data) 
      print json.dumps(parsed, indent=4, sort_keys=True)  
      print ("   " )  
channel.basic_consume(callback,
                      queue='craig',
                      no_ack=True)

channel.start_consuming()

