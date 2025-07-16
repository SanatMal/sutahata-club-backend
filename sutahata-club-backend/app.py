from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='frontend', static_url_path='/static')
CORS(app)  # Allow all origins (Netlify frontend can access)

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/login')
def login():
    return send_from_directory('frontend', 'login.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('frontend', filename)

@app.route('/api/ping')
def ping():
    return jsonify({'message': 'pong'})

@app.route('/api/login', methods=['POST'])
def login_api():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email == "admin@example.com" and password == "secret":
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/api/notices/public')
def public_notices():
    notices = [
        "Blood donation camp on 20th July",
        "Durga Puja preparation starts 1st October",
        "Tree plantation drive every Sunday"
    ]
    return jsonify(notices)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
