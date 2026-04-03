import React, { useState } from "react";
import "./App.css";

function App() {

  const [target, setTarget] = useState("");
  const [ports, setPorts] = useState([]);
  const [ip, setIp] = useState("");
  const [scannedTarget, setScannedTarget] = useState("");
  const [protocol, setProtocol] = useState("tcp");
  const [startPort, setStartPort] = useState(1);
  const [endPort, setEndPort] = useState(1024);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [mode, setMode] = useState("simple");

  const validateTarget = (value) => {

    const domainRegex = /^([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})$/;
    const ipRegex = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/;

    return domainRegex.test(value) || ipRegex.test(value);
  };

  const scanTarget = async () => {

    setError("");
    setPorts([]);
    setIp("");
    setScannedTarget("");

    if (!target) {
      setError("Enter a domain or IP");
      return;
    }

    if (!validateTarget(target)) {
      setError("Invalid domain or IP");
      return;
    }

    setLoading(true);

    try {

      const response = await fetch(
        `http://localhost:5000/scan?ip=${target}&protocol=${protocol}&start=${startPort}&end=${endPort}`
      );

      const data = await response.json();

      if (data.error) {
        setError(data.error);
      } else {
        setPorts(data.results);
        setIp(data.ip);
        setScannedTarget(data.target);
      }

    } catch (err) {
      setError("Server connection error");
    }

    setLoading(false);
  };

  return (
    <div className="App">

      <h1>Web Port Scanner</h1>

      <input
        type="text"
        placeholder="Enter IP or domain"
        value={target}
        onChange={(e) => setTarget(e.target.value)}
      />

      <br /><br />

      <label>Protocol:</label>
      <select value={protocol} onChange={(e) => setProtocol(e.target.value)}>
        <option value="tcp">TCP</option>
        <option value="udp">UDP</option>
      </select>

      <br /><br />

      <label>Mode:</label>
      <select value={mode} onChange={(e) => setMode(e.target.value)}>
        <option value="simple">Simple (Only Open)</option>
        <option value="advanced">Advanced (All Ports)</option>
      </select>

      <br /><br />
      <label>Start Port:</label>
      <input
        type="number"
        value={startPort}
        onChange={(e) => setStartPort(e.target.value)}
      />

      <label> End Port:</label>
      <input
        type="number"
        value={endPort}
        onChange={(e) => setEndPort(e.target.value)}
      />

      <br /><br />

      <button onClick={scanTarget}>
        Scan
      </button>

      <h4>
      Open: {ports.filter(p => p.state === "open").length} |
      Filtered: {ports.filter(p => p.state === "filtered").length}
      </h4>

      {loading && <p>Scanning...</p>}

      {error && <p className="error">{error}</p>}

      {scannedTarget && (
        <div>
          <h3>Target: {scannedTarget}</h3>
          <h3>IP: {ip}</h3>
        </div>
      )}

      {ports.length > 0 && (
        <div>

          <h3>Scan Results</h3>

          <table border="1" style={{ margin: "auto" }}>
            <thead>
              <tr>
                <th>Port</th>
                <th>Protocol</th>
                <th>State</th>
              </tr>
            </thead>

            <tbody>
              {ports
                .filter(p => mode === "advanced" || p.state === "open")
                .map((p, index) => (
                  <tr key={index}>
                    <td>{p.port}</td>
                    <td>{p.protocol}</td>
                    <td>{p.state}</td>
                  </tr>
                ))}
            </tbody>

          </table>

        </div>  
      )}

    </div>
  );
}

export default App;