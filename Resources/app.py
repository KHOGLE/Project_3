# This is the stuff Kyle sent me

# imports
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func
from flask import Flask,jsonify, render_template, url_for
import pandas as pd
from config import db_url

# database setup
engine = create_engine(f'{db_url}')
connection = engine.connect()

Base = automap_base()
Base.prepare(engine,reflect=True)

# table refs
MainData= Base.classes.maindata
State = Base.classes.states
Month = Base.classes.months

@app.route("/api/v1.0/maindata/")
def sightings():
     # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all sightings
    sightings_data = session.query(Sighting.date,Maindata.city,Maindata.state,Maindata.country,Maindata.shape,Maindata.duration,
                                   Maindata.summary,Maindata.latitude, Maindata.longitude).all()
    return jsonify(sightings_data)

@app.route("/")
def index():
    return render_template("index.html", pages={
        "Home": "active",
        "Page1": "",
        "Page2": "",
        "Page3": ""
    })

@app.route("/Page1/")
def page1():
    return render_template("page1.html", pages={
        "Home": "",
        "Page1": "active",
        "Page2": "",
        "Page3": ""
    })