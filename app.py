import ephem
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def hello_world():
    return 'Welcome on the ephemeris backend of NovaNet.'

# A /example végponton keresztül lehet lekérdezni a Mars helyzetét
@app.route('/api/example')
def get_example():
    # Dátum konvertálása

    date = '2024-01-01'

    try:
        observation_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return jsonify({'error': 'Érvénytelen dátum formátum'}), 400

    # Mars pozíciójának kiszámítása a megadott dátumon
    mars = ephem.Mars(observation_date)
    mars.compute(observation_date)

    # Az adatok visszaadása
    return jsonify({
        'date': date,
        'mars': {
            'right_ascension': str(mars.ra),
            'declination': str(mars.dec),
            'distance_from_sun': mars.sun_distance
        }
    })

@app.route('/api/ephemeris', methods=['POST'])
def get_ephemeris():

    data = request.get_json()

    logging.info(f"Received data: {data}")

    observation_date = '2024-01-01'

    #try:
    #    observation_date = datetime.strptime(data.observer.time, "%Y-%m-%d")
    #except ValueError:
    #    return jsonify({'error': 'Érvénytelen dátum formátum'}), 400

    # Mars pozíciójának kiszámítása a megadott dátumon
    mars = ephem.Mars(observation_date)
    mars.compute(observation_date)

    # Az adatok visszaadása
    return jsonify({
        'date': observation_date,
        'mars': {
            'right_ascension': str(mars.ra),
            'declination': str(mars.dec),
            'distance_from_sun': mars.sun_distance
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True)