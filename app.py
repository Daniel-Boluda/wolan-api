import os
import logging
from flask import Flask, request, jsonify
from wakeonlan import send_magic_packet

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuración desde variables de entorno
API_KEY = os.getenv("API_KEY", "default_key")
BROADCAST_ADDRESS = os.getenv("BROADCAST_ADDRESS", "192.168.1.255")
PORT = int(os.getenv("PORT", 9))

# Log environment variables on startup
logger.info(f"Starting Flask app with the following environment variables:")
# logger.info(f"API_KEY: {API_KEY}")
logger.info(f"BROADCAST_ADDRESS: {BROADCAST_ADDRESS}")
logger.info(f"PORT: {PORT}")

@app.route('/wake', methods=['POST'])
def wake():
    key = request.headers.get("X-API-Key")
    # print(f"Received API Key: {key}")  # Debugging line
    # print(f"Env API Key: {API_KEY}")  # Debugging line
    if key != API_KEY:
        logger.warning("Unauthorized access attempt")
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data or "mac_address" not in data:
        logger.warning("MAC address not provided in the request")
        return jsonify({"error": "MAC address is required"}), 400

    mac_address = data["mac_address"]
    logger.info(f"Sending magic packet to {mac_address}")
    send_magic_packet(mac_address, ip_address=BROADCAST_ADDRESS, port=PORT)
    logger.info(f"Magic packet sent to {mac_address}")
    return jsonify({"message": f"Paquete mágico enviado a {mac_address}"}), 200

if __name__ == '__main__':
    logger.info("Starting Flask app on 0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000)
