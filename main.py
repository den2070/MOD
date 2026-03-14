from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Список активных миров (в памяти сервера)
active_servers = set()

@app.route('/register', methods=['POST'])
def register():
    # Получаем IP игрока, который нажал "Открыть для Вторжения"
    ip = request.remote_addr 
    active_servers.add(ip)
    return jsonify({"status": "ok", "message": "World added to invasion list"}), 200

@app.route('/get_target', methods=['GET'])
def get_target():
    # Отдаем случайный IP игроку-падальщику
    if not active_servers:
        return jsonify({"status": "error", "message": "No worlds available"}), 404
    
    target_ip = random.choice(list(active_servers))
    return target_ip, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
