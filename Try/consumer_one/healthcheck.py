import pika
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="", 
    database="cc"
)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='health_check')

def callback(ch, method, properties, body):
    # Process the health check message
    # ...
    print("Received health check message: %r" % body)
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='health_check', on_message_callback=callback)

channel.start_consuming()

# Close connections
db.close()
connection.close()