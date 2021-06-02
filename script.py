import sqlite3

## define connection and cursor 

connection= sqlite3.connect("covid19_vaccination_plan.db")

##creating cursor to run the command 

c = connection.cursor()

# Create countries table 

command1= ("""CREATE TABLE IF NOT EXISTS
forecast_countries_fullyVac (location INTEGER PRIMARY KEY, fullVacNew INTEGER)""")

c.execute(command1)

command2= ("""CREATE TABLE IF NOT EXISTS
forecast_countries_vacNew (FOREIGN KEY(location) REFERENCES forecast_countries_fullyVac(location), vacNew INTEGER)""")

c.execute(command2)

command3= ("""CREATE TABLE IF NOT EXISTS
forecast_All (FOREIGN KEY(location) REFERENCES forecast_countries_fullyVac(location), vacNew INTEGER, fullVacNew INTEGER)""")

c.execute(command3)

command4= ("""CREATE TABLE IF NOT EXISTS
herd_immunity_all(FOREIGN KEY(location) REFERENCES forecast_countries_fullyVac(location), herd_immunity INTEGER)""")

c.execute(command4)

c.close()


