from flask import Flask, request, jsonify

app = Flask(__name__)

# เก็บค่าที่ต้องการส่งไปยัง ESP32
esp32_data = {"pin": 36, "state": "LOW"}

@app.route('/set_pin', methods=['POST'])
def set_pin():
    global esp32_data
    data = request.json  # รับค่า JSON
    if 'pin' in data and 'state' in data:
        esp32_data = {"pin": data["pin"], "state": data["state"]}
        return jsonify({"message": "Data updated", "data": esp32_data})
    return jsonify({"error": "Invalid request"}), 400

@app.route('/get_pin', methods=['GET'])
def get_pin():
    return jsonify(esp32_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
