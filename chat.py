import eventlet
eventlet.monkey_patch()

from random import random

from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    # get random port between 5000 and 6000
    port = int(1000 * random()) + 5000
    socketio.run(app, port=port)
