from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')


@socketio.on('join')
def handle_join(code):
    join_room(code)
    # print(f'A new user join room {code}!')


@socketio.on('leave')
def handle_leave(code):
    leave_room(code)
    # print(f'A user leave room {code}!')


@socketio.on('message')
def handle_message(data):
    # print(f'recived massage : {data}')
    code = data.get('code')
    socket_data = data.get('data')
    emit('message', {'data': socket_data}, room=code)
    # print(f'sent massage : data: {socket_data}')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
    # socketio.run(app, debug=True)
    # print('Server conected at PORT 5000 ')
