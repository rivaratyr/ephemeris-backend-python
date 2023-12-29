# Creation process

>**Python Version**: 3

## Create a Virtual Environment
`python3 -m venv venv`

Activate the virtual environment:
`source venv/bin/activate`

## Install dependencies
Make sure virtual environment is activated, then:

`pip install Flask`
`pip install ephem`

# Run app in localhost
Browse into the project's folder, then:

`python app.py`

After start there should be a message like this in the terminal:
` * Serving Flask app 'app'`
` * Debug mode: on`
` * Running on http://127.0.0.1:5000`

As the last line says, pplication is available in your browser if you visit http://127.0.0.1:5000

# Documentations
- PyEphem: https://rhodesmill.org/pyephem/quick.html

Ismerve a Föld körül keringő égitest hely- és sebességkoordinátáit egy adott időpontban, akkor tetszőleges későbbi időpontban meg kell tudni mondani, hogy hol van és mekkora a sebessége. Az elméleti háttér megtalálható az előadás anyagában, vagy Érdi Bálin Égi Mechanika , Érdi Bálint a Naprendszer dinamikája egyetemi jegyzetben vagy tankönyvben. Ezeket is feltöltöm a fenti oldalra. Ha az interneten találnak ilyen programot, és bemutatják nekem, hogy tudják használni azt is elfogadom teljes mértékben.

http://orbitsimulator.com/formulas/OrbitalElements.html
https://rhodesmill.org/skyfield/installation.html
https://exoplanetarchive.ipac.caltech.edu/docs/transit_algorithms.html#ephemeris
https://www.npmjs.com/package/astronomy
https://www.npmjs.com/package/ephemeris
https://sites.tufts.edu/eeseniordesignhandbook/files/2019/05/Krinsky-Tech-Note.pdf 

# Example TLE Data for testing

# ISS

ISS (ZARYA)             
1 25544U 98067A   21275.54627222  .00000261  00000-0  15224-4 0  9993
2 25544  51.6437  42.2009 0004280  47.2829  70.0974 15.48816821290915

## Hubble Space Telescope

HST
1 20580U 90037B   21275.18334491  .00002750  00000-0  15215-4 0  9992
2 20580  28.4690  43.4789 0002681  94.9690  54.6366 15.09712546378576

## NOAA 15 (Weather Satellite)

NOAA 15                  
1 25338U 98030A   21275.25591203 -.00000036  00000-0  33281-4 0  9996
2 25338  98.3791  37.8048 0011472 167.1828 192.9678 14.25914225225317