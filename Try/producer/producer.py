from flask import Flask, request
import pika 

app = Flask(__name__)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
@app.route('/healthcheck', methods=['GET'])
def health_check():
    # Send the health check message to the "health_check" queue
    # using the RabbitMQ client
    # ...
    channel.basic_publish(exchange='', routing_key='health_check', body='Database is healthy')
    return 'OK'

@app.route('/insertrecord', methods=['POST'])
def insert_record():
    name = request.form['Name']
    srn = request.form['SRN']
    section = request.form['Section']
    
    # Send the record data to the "insert_record" queue
    # using the RabbitMQ client
    # ...
    record_data = {'field1': 'value1', 'field2': 'value2'} # replace with actual record data
    channel.basic_publish(exchange='', routing_key='insert_record', body=str(record_data))
    return 'OK'

@app.route('/readdatabase', methods=['GET'])
def read_database():
    # Send a request to the "read_database" queue
    # using the RabbitMQ client to retrieve all records
    # from the database
    # ...
    channel.basic_publish(exchange='', routing_key='read_database', body='retrieve_all_records')
    return 'OK'

@app.route('/deleterecord', methods=['GET'])
def delete_record():
    srn = request.args.get('SRN')
    
    # Send a request to the "delete_record" queue
    # using the RabbitMQ client to delete the record
    # with the given SRN from the database
    # ...
    srn = '12345' # replace with actual SRN of record to delete
    channel.basic_publish(exchange='', routing_key='delete_record', body=srn)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)