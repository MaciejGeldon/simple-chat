import eventlet
eventlet.monkey_patch()
import json

from werkzeug.utils import redirect
from forms import LoginForm
from random import random

import redis
from flask import Flask, render_template, session, url_for, request
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, message_queue='redis://')
db = redis.StrictRedis('localhost', 6379, 0)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
    return render_template('index.html', form=form)


@app.route('/chat')
def chat():
    name = session.get('name', '')
    if name == '':
        return redirect('.index')
    return render_template('chat.html', name=name)


@socketio.on('connect')
def ws_conn():
    print('connected')
    c = db.incr('user_count')
    print(f'c {c}')
    emit('client_count', {'count': c}, broadcast=True)
    messages = db.lrange('MessagesList', 0, -1,)
    for msg in reversed(messages):
        print(f'emmiting message {msg}')
        emit('chat_message', msg)


@socketio.on('disconnect')
def ws_disconn():
    print('disconnect')
    c = db.decr('user_count')
    print(f'c {c}')
    emit('client_count', {'count': c}, broadcast=True)


@socketio.on('chat_message')
def ws_chat_message(msg):
    print('chat message event handeled')
    msg = json.dumps({'msg': msg, 'name': session.get('name')}).encode('utf-8')
    db.lpush('MessagesList', msg)
    emit('chat_message', msg, broadcast=True)


if __name__ == '__main__':
    port = int(1000 * random()) + 5000
    socketio.run(app, debug=True, port=port)
