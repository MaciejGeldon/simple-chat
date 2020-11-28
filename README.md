# Simple chat
### System requirements
This app uses Redis in two ways - as a very simple database and message queue.
Redis installation is required.


### Installation
After cloning, type:
* ``make``    
This command will create a new virtual environment and install all required packages.

### Idea    
I wanted to write a simple chat app that could be horizontally scaled.   
Most of the available tutorials I find focus either on load balancer configuration or creating simple, not horizontally scalable app made with flask and socket.io.  

Here I’ve created a horizontally scalable chat:
* The port on which the app will run is chosen randomly
* The db layer is just Redis list which will list all the messages
* The message queue for interprocess communication is also Redis

The ports are chosen randomly to easily run two or three different processes which will run on different ports. Clients don't need sticky sessions because load balancing can be done manually. Clients will connect to different ports.
This example, as crude as it is, is still able to demonstrate IPC using Redis and running chat across different processes, which for me was the main goal here.

### Sources
* https://tsh.io/blog/how-to-scale-websocket/
* https://github.com/miguelgrinberg/Flask-SocketIO-Chat
* https://socket.io/get-started/chat/