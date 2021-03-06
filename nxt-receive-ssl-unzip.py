#!/usr/bin/env python
import pika
import sys
import base64
import zlib
import gzip

import StringIO
import json
import ssl

credentials = pika.PlainCredentials('craig', 'craig')
parameters=pika.ConnectionParameters(host='10.238.131.199',
                                           port=5671,
                                           virtual_host='arrisSales',
                                           credentials=pika.PlainCredentials('craig', 'craig'),
                                           ssl=True,
                                           ssl_options={"cert_reqs": ssl.CERT_NONE, "ca_certs": 'ca_certificate_bundle.pem'})
                                           

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='tenant-out',
                         exchange_type='topic',
                         durable=True )

result = channel.queue_declare()
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s  [binding_key]\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='tenant-out',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for NXT messages. To exit press CTRL+C')

def callback(ch, method, properties, body):

      decoded_data=gzip.GzipFile(fileobj=StringIO.StringIO(body)).read()
      print(" Routing Key %r" % (method.routing_key))
      parsed = json.loads(decoded_data) 
      print json.dumps(parsed, indent=4, sort_keys=True)  
      print ("   " )  
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

