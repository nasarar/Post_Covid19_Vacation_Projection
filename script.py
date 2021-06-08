# Import required libraries
import sqlite3
import pandas as pd
  
# Connect to SQLite database
conn = sqlite3.connect('world_data_forecast.db')
c= conn.cursor()

## Execute a query 
c.execute('''CREATE TABLE world_forecast_herdimmunity (location TEXT, date TEXT, people_fully_vaccinated INT)''')

# Load CSV data into Pandas DataFrame
world_forecast_herdimmunity = pd.read_csv('Resources/world_data_forecast.csv')

# Write the data to a sqlite table
world_forecast_herdimmunity.to_sql('world_forecast_herdimmunity', conn, if_exists='append', index=False)
  
c.execute('''SELECT * FROM world_forecast_herdimmunity''').fetchall()

c.close()

#Convert the CSV to JSON string using Python 
df = pd.read_csv (r'Resources/world_data_forecast.csv')
df.to_json (r'static/world_data_forecast.json')
