from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from file_reader import FileReader

async_mode = 'gevent'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, async_mode=async_mode)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('connect')
def send_cfg():
    fr = FileReader()
    emit('cfg finsih', fr.get_all_cmd('config/steps.yaml'))
