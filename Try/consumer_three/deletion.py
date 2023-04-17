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

channel.queue_declare(queue='delete_record')

def callback(ch, method, properties, body):
    # Process the health check message
    # ...
    mycursor = db.cursor()

    sql = "DELETE FROM Customer WHERE SRN = '145'"

    mycursor.execute(sql)

    db.commit()

    print(mycursor.rowcount, "record(s) deleted")
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='delete_record', on_message_callback=callback)

channel.start_consuming()

# Close connections
db.close()
connection.close()