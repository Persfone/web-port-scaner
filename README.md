# web-port-scaner

### Low-Level Network & Vulnerability Scanner with Web Interface

---

## Overview

**web-port-scaner** es una herramienta de escaneo de red y vulnerabilidades diseñada para combinar el poder de un escáner de bajo nivel tipo Nmap con la facilidad de uso de una interfaz web moderna.

El objetivo del proyecto es crear una herramienta accesible para cualquier usuario, incluso sin conocimientos de consola, permitiendo realizar escaneos de puertos, análisis de servicios y detección básica de vulnerabilidades desde un navegador web.

La herramienta está diseñada en múltiples etapas de desarrollo, evolucionando desde un port scanner básico hasta un vulnerability scanner completo con arquitectura modular.

---

## Philosophy

El proyecto lo baso en tres pilares:

* Low-level networking (TCP, UDP, SYN, raw sockets)
* High-level accessibility (Web interface)
* Modular vulnerability analysis

La idea es democratizar el escaneo de red, permitiendo que cualquier persona pueda usar herramientas avanzadas sin necesidad de trabajar en terminal.

---

## Architecture Vision

```
User (Web Browser)
        |
        v
React Frontend
        |
        v
Flask API
        |
        v
Scanner Core (Python/C hybrid)
        |
        v
Network Engine (TCP / UDP / SYN / Raw Sockets)
        |
        v
Vulnerability Engine
        |
        v
Reports & Dashboard
```

---

# Development Stages

---

# Stage 1 — Basic Port Scanner

## Goal

Construir un escáner de puertos TCP funcional accesible desde web.

## Features

* TCP connect scan
* Domain/IP input
* Multithreading
* JSON API
* React frontend
* Open ports visualization
* Timeout handling
* DNS resolution

## Tech

* Python
* Flask
* React
* Socket
* ThreadPoolExecutor

## Output

```
Target: open.spotify.com
IP: 151.101.219.42

Open Ports
80 TCP
443 TCP
```

## Status

Completed / In Progress

---

# Stage 2 — Protocol Support

## Goal

Agregar soporte completo de protocolos.

## Features

* TCP scan
* UDP scan
* Port states

  * open
  * closed
  * filtered
  * error
* Protocol detection
* Custom port ranges

## Output

```
80 TCP open
443 TCP open
53 UDP filtered
22 TCP closed
```

## Improvements

* Faster scanning
* Better accuracy
* Protocol differentiation

---

# Stage 3 — Banner Grabbing

## Goal

Detectar servicios activos en los puertos abiertos.

## Features

* HTTP headers
* SSH banner
* FTP banner
* SMTP banner
* Service detection
* Version detection

## Output

```
80 TCP open Apache
443 TCP open nginx
22 TCP open OpenSSH 8.2
21 TCP open FTP
```

## Value

Permite identificar software vulnerable.

---

# Stage 4 — SYN Scan (Low-Level)

## Goal

Implementar escaneo SYN usando raw sockets.

## Features

* TCP SYN scan
* Packet forging
* Raw sockets
* Stealth scanning
* Faster scanning
* Linux networking

## Requirements

* Linux
* Root privileges
* cap_net_raw

## Output

```
80 TCP open (SYN)
443 TCP open (SYN)
22 TCP filtered
```

## Value

Nivel profesional de escaneo.

---

# Stage 5 — Web Scanner

## Goal

Escaneo de aplicaciones web.

## Features

* Directory fuzzing
* HTTP analysis
* Headers security
* XSS detection
* SQL injection tests
* CMS detection

## Output

```
/admin found
/login found
XSS possible
SQL injection possible
Missing CSP header
```

---

# Stage 6 — Vulnerability Engine

## Goal

Motor de detección de vulnerabilidades.

## Features

* Service-based rules
* Port-based analysis
* CVE mapping
* Risk scoring
* Fingerprinting
* OS detection
* CMS detection

## Output

```
Apache 2.4 -> outdated
OpenSSH -> secure
FTP -> anonymous login possible

Risk Score: Medium
```

---

# Stage 7 — Reporting System

## Goal

Generar reportes profesionales.

## Features

* JSON report
* HTML report
* PDF report
* Scan summary
* Risk level
* Port summary
* Vulnerability summary

## Output

```
scan_report.html
scan_report.json
scan_report.pdf
```

---

# Stage 8 — Threat Intelligence

## Goal

Integración con inteligencia de amenazas.

## Features

* Blacklist IP check
* IOC feeds
* Known malicious hosts
* Reputation system

## Output

```
Target flagged in blacklist
Risk: High
```

---

# Stage 9 — CLI + Web Hybrid

## Goal

Uso dual.

## CLI

```
vulnscanner scan google.com
```

## Web

```
http://localhost:3000
```

## Value

Herramienta profesional y accesible.

---

# Stage 10 — Full Vulnerability Scanner

## Final Goal

Crear una herramienta completa:

* Low-level network scanner
* Web vulnerability scanner
* GUI
* API
* Reporting
* Threat intelligence
* Modular engine

---

# Tech Stack

## Frontend

React
CSS
Axios

## Backend

Flask
Python

## Low-Level Scanner

C
Sockets
Raw sockets
Threads

## Networking

TCP
UDP
SYN
HTTP

## Future

Rust or C core engine

---

# Project Structure

```
vulnscanner/

frontend/
react app

backend/
flask api

scanner/
tcp scan
udp scan
syn scan

engine/
vulnerability engine

reports/
html json pdf

docs/
readme
architecture
```

---

# Goal

Crear una herramienta de ciberseguridad que:

* sea poderosa como un scanner profesional
* sea accesible como una web app
* sea modular
* sea open source
* sea educativa
* sea usable por cualquier persona

---

# Vision

Una herramienta de escaneo de red y vulnerabilidades que combine:

Low-level power
High-level usability
Security analysis
Modern web interface

Todo en una sola plataforma.

