import os
from flask import Flask, request, jsonify
from wakeonlan import send_magic_packet

app = Flask(__name__)

# Configuración desde variables de entorno
API_KEY = os.getenv("API_KEY", "default_key")
BROADCAST_ADDRESS = os.getenv("BROADCAST_ADDRESS", "192.168.1.255")
PORT = int(os.getenv("PORT", 9))

@app.route('/wake', methods=['POST'])
def wake():
    key = request.headers.get("X-API-Key")
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data or "mac_address" not in data:
        return jsonify({"error": "MAC address is required"}), 400

    mac_address = data["mac_address"]
    send_magic_packet(mac_address, ip_address=BROADCAST_ADDRESS, port=PORT)
    return jsonify({"message": f"Paquete mágico enviado a {mac_address}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
