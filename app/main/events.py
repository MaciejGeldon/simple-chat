import json

from flask import session
from flask_socketio import emit

from app import socketio
from app.main.db import db


@socketio.on('connect')
def ws_conn():
    c = db.incr('user_count')
    emit('client_count', {'count': c}, broadcast=True)
    messages = db.lrange('MessagesList', 0, -1,)
    for msg in reversed(messages):
        emit('chat_message', msg)


@socketio.on('disconnect')
def ws_disconn():
    c = db.decr('user_count')
    emit('client_count', {'count': c}, broadcast=True)


@socketio.on('chat_message')
def ws_chat_message(msg):
    msg = json.dumps({'msg': msg, 'name': session.get('name')}).encode('utf-8')
    db.lpush('MessagesList', msg)
    emit('chat_message', msg, broadcast=True)