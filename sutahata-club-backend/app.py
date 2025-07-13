from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='frontend', static_url_path='/static')

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/login')
def login():
    return send_from_directory('frontend', 'login.html')

@app.route('/api/ping')
def ping():
    return jsonify({'message': 'pong'})

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('frontend', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
