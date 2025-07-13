from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='frontend', static_url_path='/static')

# Serve the home page
@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

# Serve the login page
@app.route('/login')
def login():
    return send_from_directory('frontend', 'login.html')

# Example API route
@app.route('/api/ping')
def ping():
    return jsonify({'message': 'pong'})

# Serve static files like CSS, JS, images
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('frontend', filename)

# Optional: For debugging on development server
if __name__ == '__main__':
    app.run(debug=True)
