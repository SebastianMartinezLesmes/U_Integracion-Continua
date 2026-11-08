
from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

SERVICIO_1_URL = os.getenv(
    "SERVICIO_1_URL",
    "http://servicio-1:5000"
)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "servicio": "Servicio 2",
        "estado": "Funcionando",
        "mensaje": "API consumidora ejecutándose correctamente"
    })


@app.route("/api/comunicacion", methods=["GET"])
def comunicacion():
    try:
        respuesta = requests.get(
            f"{SERVICIO_1_URL}/api/saludo",
            timeout=5
        )

        respuesta.raise_for_status()

        return jsonify({
            "estado": "Exitoso",
            "servicio_origen": "Servicio 2",
            "servicio_destino": "Servicio 1",
            "respuesta_servicio_1": respuesta.json()
        })

    except requests.exceptions.RequestException as error:
        return jsonify({
            "estado": "Error",
            "mensaje": "No fue posible comunicarse con el Servicio 1",
            "detalle": str(error)
        }), 503


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "estado": "healthy",
        "servicio": "servicio-2"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
