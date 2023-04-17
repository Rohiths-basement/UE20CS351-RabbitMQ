import pika
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="", 
    database="cc"
)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='read_database')

def callback(ch, method, properties, body):
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM Customer")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='read_database', on_message_callback=callback)

channel.start_consuming()

# Close connections
mydb.close()
connection.close()