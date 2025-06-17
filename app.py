from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return "¡Hola desde Flask desplegado en Railway!"

@app.route("/hola")
def saludo():
    return "¡Esta es un ruta personalizada!"

@app.route("/api/pagos_pendientes")
def obtener_pagos():
    pagos = [
        {
            "numSocio": 1001,
            "importe": 35.00,
            "fechaExp": "2025-06-14",
            "fechaPago": "2025-06-15",
            "fechaVto": "2025-07-15",
            "numCuota": 3,
            "formaPago": "tarjeta",
            "idPago": "abs123"
        },
        {
            "numSocio": 1002,
            "importe": 50.00,
            "fechaExp": "2025-06-14",
            "fechaPago": "2025-06-16",
            "fechaVto": "2025-07-16",
            "numCuota": 2,
            "formaPago": "bizum",
            "idPago": "abc002"
        }
    ]
    return jsonify(pagos)

@app.route("/clientes")
def clientes():
    lista_clientes = [
        {"id": 1, "nombre": "Carlos Pérez", "activo": True},
        {"id": 2, "nombre": "Laura Gómez", "activo": False},
        {"id": 3, "nombre": "Andrea Ruiz", "activo": True}
    ]
    return jsonify(lista_clientes)

@app.route("/api/marcar_pagado", methods=["POST"])
def marcar_pagado():
    data = request.get_json()
    id_pago = data.get("idPago")
    print(f"Pago sincronizado en la nube: {id_pago}")
    return jsonify({"mensaje": "Pago sincronizado con éxito"}), 200