from flask import Flask, request, jsonify

app = Flask(__name__)

# Хранение команд в очереди игры (просто для примера, в реальной системе используйте более надежное хранилище)
game_commands = {}

@app.route('/receive_message', methods=['POST'])
def receive_message():
    try:
        data = request.get_json()

        # Извлечь данные из JSON-сообщения
        game_id = data.get('game_id')
        object_id = data.get('object_id')
        operation_id = data.get('operation_id')
        args = data.get('args')

        # Ваш код маршрутизации команды внутри игры

        # Пример: поместить команду в очередь игры
        command = {
            'object_id': object_id,
            'operation_id': operation_id,
            'args': args
        }
        if game_id in game_commands:
            game_commands[game_id].append(command)
        else:
            game_commands[game_id] = [command]

        return jsonify({"message": "Command received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
