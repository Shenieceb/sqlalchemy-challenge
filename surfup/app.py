# Import the dependencies.

from flask import Flask, jsonify
import datetime as dt
from dateutil.relativedelta import relativedelta

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func



#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with= engine)

# reflect an existing database into a new model

# reflect the tables


# Save references to each table

Station = Base.classes.station
Measurement = Base.classes.measurement


# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
 return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(tobs)    

@app.route("/api/v1.0/temp/<start>")
def start():
    return jsonify(start)

@app.route("/api/v1.0/temp/<start>/<end>")
def start_end():
    return jsonify(start_end)

if __name__ == '__main__':
    app.run(debug=True)