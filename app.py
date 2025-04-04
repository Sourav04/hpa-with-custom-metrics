from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Define a Prometheus Counter to track HTTP requests
http_requests = Counter('http_request_count', 'Total HTTP requests received')

@app.route('/')
def home():
    http_requests.inc()  # Increment the counter
    return "Hello, World!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
