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
