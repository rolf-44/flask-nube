from flask import Flask, jsonify, request
import mysql.connector
from datetime import date

app = Flask(__name__)

# configuración de conexión remota (Railway)
DB_REMOTE = {
    "host": "mysql.railway",
    "user": "root",
    "password": "atIaVlkODsRRqpXsmjRHbxncuPKbshyi",
    "database": "railway"
}

# Función auxiliar para connectar
def get_connection():
    return mysql.connector.connect(**DB_REMOTE)

# Ruta 1: Obtener información del socio
@app.route("/api/socio/<int:numSocio>")
def obtener_socio(numsocio):
    try:
        conn = get_connection()
        cursor = conn.cursor(directory=True)

        cursor.execute("""
            SELECT 
                s.numsocio, 
                s.nombre, 
                s.fechaVto, 
                s.numCuota, 
                s.precioEsp,
                s.precio
                c.precio as preCuota, 
                c.tipoprecio,
                c.sesiones,
                c.semanas,
                c.meses    
            FROM Socios s
            JOIN Cuotas c ON s.numCuota=c.numCuota) 
            WHERE numSocio = %s
            ORDER BY s.fechaVto DESC LIMIT 1
        """, (numSocio,))

        socio = cursor.fetchone()
        cursor.close()

        if socio:
            return jsonify(socio)
        else:
            return jsonify({"error": "Socio no encontrado"})
    except Exception as e:
        return jsonify({Eerror": f"Error al obtener datos del socio: {e})},500

def inicio():
    return "¡Hola desde Flask desplegado en Railway!"

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