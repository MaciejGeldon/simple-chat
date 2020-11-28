# Simple chat
### System requirements
Redis is used in this app as both very simple database and message queue.   
Installing redis is required.

### Installation
After cloning, type:
* ``make``    
This command will create new virtual environment and install all required packages.

### Idea    
I wanted to write simple chat app that could be horizontally scaled.    
Most of the tutorials I find focused either on load balancer configuration or on how to write simple 
not horizontally scalable app in flask with flask and socket io.    

Here I made horizontally scalable chat:
* The port on which the app will run is chosen randomly
* The db layer is just redis list which will list all the messages
* The message queue for interprocess communication is also redis

The ports are chosen at random to easily run two or three different processes.
Which will run on different ports, client don't need sticky sessions because load balancing can be done 
manually. Clients will connect to different ports.    
This example as crude as it is is still able to demonstrate IPC using redis, and running chat across 
different processes which for me was the main goal here.

### Sources
* https://tsh.io/blog/how-to-scale-websocket/
* https://github.com/miguelgrinberg/Flask-SocketIO-Chat
* https://socket.io/get-started/chat/