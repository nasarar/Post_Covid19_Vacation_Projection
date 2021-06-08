#Import Dependencies 
from flask import Flask


#Adding sqlalchemy dependencies
from sqlalchemy.schema import MetaData, Table
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session


#Create a new flask app
app= Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///world_data_forecast.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy()
# db.init_app(app)

# #Setting up Database
# engine=create_engine("sqlite:///world_data_forecast.db")

# #connection to engine 
# connection= engine.connect()

# #Creating Session: 
# session=Session(engine)

# Route created to connect to db
@app.route('/')
def index():
    #Setting up Database
    engine=create_engine("sqlite:///world_data_forecast.db")

    #connection to engine 
    connection= engine.connect()

    #Creating Session: 
    session=Session(engine)
    
    # metadata = MetaData()
    # WorldDataForecast = Table('world_data_forecast', metadata, autoload=True, autoload_with=session)
    # result = session.query(WorldDataForecast).all()
    result = connection.execute('select * from world_data_forecast')
    result_json = []
    for row in result.fetchall():
        result_json.append({
        'date': row[0],
        'date_adjusted': row[1],
        'people_fully_vaccinated' : row[2],
        'location': row[3],
        
    })

    return render_template("index2.html", results_json=results_json )


