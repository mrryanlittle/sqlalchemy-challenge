import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import create_engine, func
from flask import Flask, jsonify

# Database Setup
engine = create_engine('sqlite:////Resources.hawaii.sqlite')
# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Flask Setuip
app = Flask(__name__)
#Flask Routes

@app.route('/')
def index():
    return (f'Available Routes:<br/>'
            f'/api/v1.0/precipitation<br/>'
            f'/api/v1.0/stations<br/>'
            f'/api/v1.0/tobs<br/>')

@app.route('/api/v1.0/precipitation')
    session = Session(engine)
    prcp_results = session.query(Measurement.date, Measurement.prcp).all()
    session.close
    prcp_dict = list(np.ravel(prcp_results))
    return jsonify(prcp_results)

@app.route('/api/v1.0/stations')
    session = Session(engine)
    stations_results = session.query(Station.name).all()
    session.close
    stations_dict = list(np.ravel(prcp_results))
    return jsonify(stations_results)

@app.route('/api/v1.0/tobs')
    session = Session(engine)
    tobs_results = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date > '2016-08-24').all()
    session.close
    tobs_dict = list(np.ravel(prcp_results))
    return jsonify(tobs_results)

if __name__ == '__main__':
    app.run(debug=True)