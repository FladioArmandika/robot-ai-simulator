from flask import Flask, render_template, Response, request, jsonify, after_this_request
from flask_socketio import SocketIO, emit
import os
from flask_cors import CORS, cross_origin
import random


app = Flask(__name__)
cors = CORS(app)

app.config['SECRET_KEY'] = 'ivangunawan'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robot')
def robot():
    return render_template('robot.html')

@app.route('/analyze')
def analyze():
    data = ["1","2","3","4"]
    n = random.randint(0,3)
    socketio.emit('sendto robot', data[n], broadcast=True)
    return "analyze";

# SOCKET
@socketio.on('analyze')
def handle_message(message):
    print('received message: ' + str(message))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    socketio.run(app)
    app.run(debug=True)
