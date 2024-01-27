from flask import Flask, request, jsonify
from multiprocessing import Pool, cpu_count
import subprocess
import socket

app = Flask(__name__)

def stress_cpu(n):
    total = 0
    for i in range(n):
        total += i**2
    return total

@app.route('/', methods=['POST', 'GET'])
def handle_request():
    if request.method == 'POST':
        # Handle POST request to stress the CPU
        try:
            # Create a separate process to run stress_cpu.py
            subprocess.Popen(["python3", "stress_cpu.py"])
            return jsonify({"message": "CPU stress initiated"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'GET':
        # Handle GET request to return the private IP address
        private_ip = socket.gethostbyname(socket.gethostname())
        return jsonify({"private_ip": private_ip}), 200

if __name__ == "__main__":
    # Run the Flask app on port 5000
    app.run(host="0.0.0.0", port=5000)
