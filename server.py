from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

locations = {}

@app.route('/location', methods=['POST'])
def update_location():
    data = request.json
    device_id = data.get('device_id')
    if device_id:
        locations[device_id] = {
            'lat': data['lat'],
            'lon': data['lon'],
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify({'status': 'ok'})
    return jsonify({'error': 'Missing device_id'}), 400

@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify(locations)

@app.route('/map')
def serve_map():
    return send_from_directory('static', 'map.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
