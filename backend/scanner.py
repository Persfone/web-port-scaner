from flask import Flask, request, jsonify
from flask_cors import CORS
import socket
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
CORS(app)


# ---------------- TCP SCAN ----------------

def scan_tcp(ip, port, timeout):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)

        result = s.connect_ex((ip, port))
        s.close()

        if result == 0:
            state = "open"
        elif result == 111:
            state = "closed"
        else:
            state = "filtered"

        return {
            "port": port,
            "protocol": "TCP",
            "state": state
        }

    except:
        return {
            "port": port,
            "protocol": "TCP",
            "state": "error"
        }


# ---------------- UDP SCAN ----------------

def scan_udp(ip, port, timeout):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(timeout)

        s.sendto(b"test", (ip, port))

        try:
            data, _ = s.recvfrom(1024)
            state = "open"
        except socket.timeout:
            state = "filtered"

        s.close()

        return {
            "port": port,
            "protocol": "UDP",
            "state": state
        }

    except:
        return {
            "port": port,
            "protocol": "UDP",
            "state": "error"
        }


# ---------------- CORE SCANNER ----------------

def scan_ports(target, protocol, start, end, threads, timeout):

    open_ports = []

    try:
        ip = socket.gethostbyname(target)
    except:
        return []

    ports = range(start, end)

    with ThreadPoolExecutor(max_workers=threads) as executor:

        if protocol == "tcp":
            results = executor.map(lambda p: scan_tcp(ip, p, timeout), ports)

        elif protocol == "udp":
            results = executor.map(lambda p: scan_udp(ip, p, timeout), ports)

        else:
            return []

    for r in results:
        open_ports.append(r)

    return open_ports


# ---------------- API ----------------

@app.route("/scan")
def scan():

    target = request.args.get("ip")
    protocol = request.args.get("protocol", "tcp")
    start = int(request.args.get("start", 1))
    end = int(request.args.get("end", 1024))
    threads = int(request.args.get("threads", 50))
    timeout = float(request.args.get("timeout", 0.5))

    if not target:
        return jsonify({"error": "No target provided"})

    try:
        ip = socket.gethostbyname(target)
    except:
        return jsonify({"error": "Invalid domain or DNS error"})

    results = scan_ports(target, protocol, start, end, threads, timeout)

    return jsonify({
        "target": target.upper(),
        "ip": ip,
        "protocol": protocol.upper(),
        "range": f"{start}-{end}",
        "results": results
    })


app.run(host="0.0.0.0", port=5000)