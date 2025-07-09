from flask import Flask, request
import socket
from datetime import datetime
 
app = Flask(__name__)
 
@app.route('/')
def index():
    pod_ip = request.remote_addr
    pod_name = socket.gethostname()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    uri = request.url
    return {
        "Pod IP": pod_ip,
        "Pod Name": pod_name,
        "Current Time": current_time,
        "URI": uri
    }
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
