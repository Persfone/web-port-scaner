from flask import Flask, request, jsonify
from flask_cors import CORS
import socket
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
CORS(app)


def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip, port))
        s.close()

        if result == 0:
            return port

    except:
        return None


def scan_ports(target):

    open_ports = []

    try:
        ip = socket.gethostbyname(target)
    except:
        return []

    with ThreadPoolExecutor(max_workers=50) as executor: #concurrencia de hasta 50
        results = executor.map(lambda p: scan_port(ip, p), range(1, 1024)) # deteccion de puertos tipicos y puertos bien conocidos

    for r in results:
        if r:
            open_ports.append(r)

    open_ports.sort()

    return open_ports


@app.route("/scan")
def scan():

    target = request.args.get("ip")

    if not target:
        return jsonify({"error": "No target provided"})

    try:
        ip = socket.gethostbyname(target)
    except:
        return jsonify({"error": "Invalid domain or DNS error"})

    ports = scan_ports(target)

    return jsonify({ 
        "target": target.upper(),
        "ip": ip, 
        "open_ports": ports
    })


app.run(host="0.0.0.0", port=5000)