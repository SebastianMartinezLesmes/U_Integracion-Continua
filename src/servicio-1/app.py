
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "servicio": "Servicio 1",
        "estado": "Funcionando",
        "mensaje": "API principal ejecutándose correctamente"
    })


@app.route("/api/info", methods=["GET"])
def info():
    return jsonify({
        "servicio": "Servicio 1",
        "descripcion": "API principal del proyecto de Integración Continua",
        "fecha": datetime.now().isoformat(),
        "estado": "Disponible"
    })


@app.route("/api/saludo", methods=["GET"])
def saludo():
    return jsonify({
        "servicio": "Servicio 1",
        "mensaje": "Hola desde el Servicio 1",
        "respuesta": "Comunicación entre contenedores exitosa"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "estado": "healthy",
        "servicio": "servicio-1"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
