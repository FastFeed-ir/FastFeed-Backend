from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(code):
    join_room(code)
    print(f'A new user join room {code}!')

@socketio.on('leave')
def handle_leave(code):
    leave_room(code)
    print(f'A user leave room {code}!')


@socketio.on('message')
def handle_message(data):
    message = data.get('message')
    code = data.get('code')
    print(f'recived massage : {data}')
    if message and code:
        emit('message', {'message': message}, room=code)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
    print('Server conected at PORT 5000 ')

