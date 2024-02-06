Docker Connection Guide
Overview
This guide outlines the steps to connect two Python applications running in separate Docker containers. One application acts as a server, and the other as a client.

Prerequisites
Docker installed on your machine.
Basic understanding of Docker containerization.
Python applications prepared for containerization.
Steps
Step 1: Create a Docker Network
Create a custom network to facilitate communication between containers.

bash
Copy code
docker network create my_network
Step 2: Build Docker Images
Ensure you have Docker images for both the server and client applications. You can build images using Dockerfiles.

bash
Copy code
docker build -f Docker.tws_simulator -t server-app . 
docker build -f Dockerfile.helper_simulator -t helper-simulator-app .

Step 3: Run Server Container
Start the server container on the custom network. Ensure the server is listening on 0.0.0.0.

bash
Copy code
docker run --network my-network -p 8496:8496 --name server-app server-app
Step 4: Run Client Container
Start the client container on the same network. The client should connect to the server using the server container's name.

Copy code
docker run --network my-network helper-simulator-app
Step 5: Client Script Configuration
Modify the client script to connect to the server using the server container's hostname (server_container in this guide).

