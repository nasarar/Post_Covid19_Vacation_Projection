#Import Dependencies
from flask import Flask, render_template

#Adding sqlalchemy dependencies
from sqlalchemy.schema import MetaData, Table
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session


#Create a new flask app
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///world_data_forecast.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)


def get_data():
    """
    Get data from database (returning all).
    """
    metadata = MetaData()
    WorldDataForecast = Table(
        'world_forecast_herdimmunity',
        metadata,
        autoload=True,
        autoload_with=db.engine
    )
    result = db.session.query(WorldDataForecast).all()

    result_json = []
    for row in result:
        result_json.append({
        'date': row.date,
        'date_adjusted': row.date_adjusted,
        'people_fully_vaccinated' : row.people_fully_vaccinated,
        'location': row.location,

    })
    return result_json

# Route created to connect to db
@app.route('/')
def index():
    result_json = get_data()
    return render_template("index2.html", result_json=result_json )


@app.route('/vaccination-data')
def vaccination_data():
    result_json = get_data()
    return render_template("index.html", result_json=result_json )
