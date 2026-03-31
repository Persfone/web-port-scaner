from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

def scan_ports(target):

    open_ports = []

    for port in range(20, 100):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)

        s.close()

    return open_ports


@app.route("/scan")
def scan():

    ip = request.args.get("ip")

    ports = scan_ports(ip)

    return jsonify(ports)


app.run(host="0.0.0.0", port=5000)