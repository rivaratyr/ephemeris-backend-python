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

    try:
        # Defining the observer (from Earth)
        observer = ephem.Observer()
        observer.lon = data["data"]["observer"]["longitude"]
        observer.lat = data["data"]["observer"]["latitude"]
        observer.elevation = int(data["data"]["observer"]["elevation"])
        observer.date = data["data"]["observer"]["time"]

        # Defining the bidy to be observed by TLE data
        line1 = data["data"]["body"]["tle1"]
        line2 = data["data"]["body"]["tle2"]
        line3 = data["data"]["body"]["tle3"]
        body = ephem.readtle(line1, line2, line3)
        body.compute(observer)
        print('%s %s' % (body.sublong, body.sublat))

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Az adatok visszaadása
    return jsonify({
        'date': observer.date,
        'body': {
            'right_ascension': str(body.ra),
            'declination': str(body.dec),
            'azimuth': body.az,
            'altitude': body.alt,
            'distance_from_observer': body.range,
            'subpoint_longitude': body.sublong,
            'subpoint_latitude': body.sublat,
            'subpoint_elevation': body.elevation
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True)