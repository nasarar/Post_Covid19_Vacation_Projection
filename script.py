# Import required libraries
import sqlite3
import pandas as pd
  
# Connect to SQLite database
conn = sqlite3.connect('forecast_all.db')
c= conn.cursor()

## Execute a query 
c.execute('''CREATE TABLE forecast_herdimmunity (country TEXT, date TEXT, prediction INT)''')

# Load CSV data into Pandas DataFrame
forecast_herdimmunity = pd.read_csv('Resources/---.csv')

# Write the data to a sqlite table
forecast_herdimmunity.to_sql('forecast_herdimmunity', conn, if_exists='append', index=False)
  
c.execute('''SELECT * FROM forecast_herdimmunity''').fetchall()

c.close()



