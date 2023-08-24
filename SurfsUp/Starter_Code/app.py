# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func 
import datetime as dt

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
#create engine - tells program where database file is
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
# Declare a Base using 'automap_base()'
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################


#2. Create an app, being sure to pass __name__
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
#3. Define what to do when a user hits the index route

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>"

    )

date_one_year_ago  = dt.date(2017, 8, 23) - dt.timedelta(days=365)
query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= date_one_year_ago).all()
query_results = dict(query)
query_results
@app.route("/api/v1.0/precipitation")
def precipitation():
    return query_results


# active_query = session.query((Measurement.station),func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
# @app.route("/api/v1.0/stations")
# def stations():
#     return jsonify(active_query)

# @app.route("/api/v1.0/tobs")

# @app.route("/api/v1.0/<start>")

# @app.route("/api/v1.0/<start>/<end>")

if __name__ =="__main__":
    app.run(debug=True)