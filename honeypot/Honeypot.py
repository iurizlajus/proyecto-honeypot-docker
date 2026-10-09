from flask import Flask, request, render_template
import logging
import os
import datetime

app = Flask(__name__)

# Crea la carpeta de logs si no existe
os.makedirs('/app/logs', exist_ok=True)

# Configuración del archivo Log que leerá Checkmk
logging.basicConfig(
    filename='/app/logs/honeypot_auth.log', 
    level=logging.INFO,
    format='%(asctime)s - ALERTA DE SEGURIDAD - %(message)s'
)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')

        # Capturamos la IP real que Nginx nos está pasando
        ip = request.headers.get('X-Real-IP', request.remote_addr)

        # Guardamos el intento malicioso en el archivo de logs
        logging.info(f"IP: {ip} | Intento de login | Usuario: '{user}' | Password: '{password}'")

        # Siempre denegamos el acceso simulando una caída de base de datos
        error_msg = "Database connection failed - Error 1045: Access denied for user."
        return render_template('index.html', error=error_msg)

    return render_template('index.html')

if __name__ == '__main__':
    # Ejecuta el servidor web escuchando en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
