import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask,jsonify, render_template, url_for
import pandas as pd

engine = sqlalchemy.create_engine("sqlite:///business_data.db", echo=False)

Base = automap_base()
Base.prepare(autoload_with=engine)
full_data = Base.classes.business_data

app = Flask(__name__)

@app.route("/api/v1.0/full_data.json")
def data():
    results = engine.execute("select * from business_data")
    return jsonify([dict(i) for i in results])

if __name__ == "__main__":
    app.run(debug=True)