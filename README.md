# Wake-on-LAN API

## Overview

Wake-on-LAN API is a lightweight Flask-based application that allows you to send magic packets to wake up devices on your network. It runs inside a Docker container and exposes an HTTP endpoint to trigger Wake-on-LAN (WoL) functionality securely using an API key.

## Features

- Secure API key authentication
- Sends Wake-on-LAN magic packets to specified MAC addresses
- Configurable broadcast address and port via environment variables
- Runs in a Docker container for easy deployment
- Simple REST API with JSON request support

## Prerequisites

- Docker installed on your system
- A device that supports Wake-on-LAN
- The MAC address of the target device

## Configuration

The application uses environment variables for configuration. You can set them in a `.env` file or pass them as arguments when running the container.

- `API_KEY`: API key required to authenticate requests
- `BROADCAST_ADDRESS`: The network broadcast address (default: `192.168.1.255`)
- `PORT`: The UDP port used for Wake-on-LAN (default: `9`)

## Building the Docker Image

To build the Docker image:

```bash
docker build -t wakeonlan-api .
```

## Docker Compose Configuration

To deploy the API using Docker Compose:

```yaml
version: "3.8"

services:
  wol_api:
    image: docker.io/bolferdocker/wolan-api:0.0.2
    network_mode: host
    environment:
      - API_KEY=default_key
      - BROADCAST_ADDRESS=192.168.1.255
      - PORT=9
    restart: unless-stopped
```

network_mode: host allows the container to use the host's network stack

## Making a Request to the API

Once the Docker container is running, you can interact with the API by sending a POST request to the /wake endpoint.

Here's an example of how to make a request using PowerShell on Windows:


```powershell
Invoke-RestMethod -Uri "http://192.168.1.248:5000/wake" `
    -Method POST `
    -Headers @{"X-API-Key"="default_key"; "Content-Type"="application/json"} `
    -Body '{"mac_address": "E8-9C-25-DD-C0-2A"}'
```

This request will trigger the Wake-on-LAN process for the provided MAC address.