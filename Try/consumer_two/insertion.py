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

channel.queue_declare(queue='insert_record')

def callback(ch, method, properties, body):
    # Process the health check message
    # ...
    mycursor = db.cursor()
    sql = "INSERT INTO Customer (SRN) VALUES (%s)"
    val = ("145")
    mycursor.execute(sql, val)

    db.commit()
    print(mycursor.rowcount, "record inserted.")
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='insert_record', on_message_callback=callback)

channel.start_consuming()

# Close connections
db.close()
connection.close()