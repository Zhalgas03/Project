# Project



# Introduction
Problem Description:
With the increasing adoption of IoT devices, the amount of data generated has grown exponentially. Efficient systems are necessary for managing and analyzing this big data to extract valuable insights and make informed decisions.

Project Objective:
The objective of this project is to develop an integrated system that uses an MQTT server and Python to receive, process, and store data from IoT sensors in various databases. The databases include MySQL for structured data, MongoDB for unstructured data, and Neo4j for graph-based data storage. The system will process and store the data based on the topic of the MQTT messages.




# Implementation of MQTT Server
Selecting an MQTT Server:
I selected HiveMQ as the MQTT server for this project due to its high performance, scalability, and ability to handle large volumes of data effectively.

Server Configuration:
I configured the HiveMQ broker to receive and forward MQTT messages from IoT devices. The broker was set up to listen on the default MQTT port and handle message traffic efficiently.




# Python Application Development
Using the Paho MQTT Library:
I used the Paho MQTT library to develop a Python application capable of connecting to the HiveMQ broker and subscribing to specific topics to receive data.

Data Processing:
The application processes the received MQTT messages, transforming them into a format suitable for storage and analysis.




# Database Integration
Database Selection:
I chose the following databases to store IoT data based on their characteristics and requirements:

  MySQL for structured relational data.
  MongoDB for unstructured or semi-structured data.
  Neo4j for graph-based data storage.

Connection to Databases:
I implemented connections to these databases using specific libraries:
  mysql.connector for MySQL
  pymongo for MongoDB
  neo4j Python driver for Neo4j
Data Writing:
I defined the logic to write processed data into the respective databases based on the MQTT message topics. For example, sensor data like temperature and humidity is stored in MySQL, while network data is stored in Neo4j.




# Test and Evaluation
Functional Tests:
I verified the correct functioning of the system through a series of tests that included data reception, processing, and storage in MySQL, MongoDB, and Neo4j databases.

Performance Evaluation:
I measured the system's performance in terms of data processing speed, scalability, and reliability under different loads.




#  Conclusions
Summary of Results:
The project successfully developed a system integrating MQTT with MySQL, MongoDB, and Neo4j. The system demonstrated efficient data handling and storage capabilities across different database platforms.

Possible Future Developments:
Potential areas for improvement and extension include:
  Implementing advanced data analytics and visualization.
  Enhancing security features for data transmission and storage.
  Exploring additional database integrations.




# Documentation and Presentation
Technical Documentation:
I created detailed documentation that includes the system architecture, the technologies used, and instructions for installation and use.

Project Presentation:
I prepared a presentation illustrating the project objectives, implementation, and results obtained, to share with faculty and colleagues.
