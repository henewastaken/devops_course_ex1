import subprocess
import socket
import psutil
import requests
from flask import Flask, jsonify

app = Flask(__name__)

def get_ip():
    return socket.gethostbyname(socket.gethostname())

def get_running_processes():  
    return subprocess.getoutput("ps -ax")

def get_disk_space():
    return psutil.disk_usage('/').free


def get_uptime():
    return psutil.boot_time()

@app.route('/')
def service1_info():
    service2_url = 'http://service2:8200'
    try:
        service2_response = requests.get(service2_url)
        service2_info = service2_response.json()
    except requests.exceptions.RequestException as e:
        service2_info = {'error': 'Unable to reach Service2', 'details': str(e)}

    service1_info = {
        'service': 'Service1',
        'ip_address': get_ip(),
        'running_processes': get_running_processes(),
        'free_disk_space': get_disk_space(),
        'uptime': get_uptime(),
    }

    return jsonify({
        'service1': service1_info,
        'service2': service2_info
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8199)
