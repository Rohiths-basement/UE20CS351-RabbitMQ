# UE20CS351-RabbitMQ
This project is done as part of the academic course "Cloud Computing" with course code UE20CS351 at PES University in the 6th semester.

The aim of this project was to understand microservices communication using RabbitMQ

# Problem Statement:
Building and deploying a microservices architecture where multiple components communicate with each other using RabbitMQ. ( RabbitMQ is a  message broker which is an architectural pattern for message validation, transformation and routing) For the scope of this project, we will build 4 microservices: A HTTP server that handles incoming requests to perform CRUD operations on a Student Management Database + Check the health of the RabbitMQ connection, a microservice that acts as the health check endpoint, a microservice that inserts a single student record, a microservice that retrieves student records, a microservice that deletes a student record given the SRN.


# File Structure 
├── <microservices-project-directory>
    ├── docker-compose.yml
    ├── producer
    │   ├── producer.py
    │   ├── Dockerfile
        └──requirements.txt
    ├── consumer_one
    │   ├── healthcheck.py
    │   ├── Dockerfile
    │   └──requirements.txt
    ├── consumer_two
    │   ├── insertion.py
    │   ├── Dockerfile
    │   └──requirements.txt
    ├── consumer_three
    │   ├── deletion.py
    │   ├── Dockerfile
    │   └──requirements.txt
    └── consumer_four
        ├── read.py
        ├── Dockerfile
        └──requirements.txt
