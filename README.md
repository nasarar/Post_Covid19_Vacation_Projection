# Post COVID-19 Vacation Projection 

## Selected topic

-	Help travellers plan their next vacation by determining when countries will reach herd immunity based on their current vaccination rate. 

## Reason we selected the topic: 

-	COVID-19 has impacted many people around the world and many people are eager to travel. A major barrier to travelling right now is safety. Based on the current vaccination rates in each country we are going to determine when each country will reach herd immunity. Herd immunity is reached when approximately 70% of the population is fully vaccinated. 

## Description of the source of data: 

- Data is being used from Our World in Data for all countries but firstly to test our model, we will be using 3 countries. 
- Website: https://ourworldindata.org/covid-vaccinations

Mathieu, E., Ritchie, H., Ortiz-Ospina, E. et al. A global database of COVID-19 vaccinations. Nat Hum Behav (2021). https://doi.org/10.1038/s41562-021-01122-8

## Defining the problem we plan to solve.
-	When will countries reach herd immunity for safe travelling? 

<<<<<<< HEAD
## Defining the problem we plan to solve
•	When will countries reach herd immunity for safe travelling? 

## Project: Interactive website for Post COVID-19 Vacation Planner

•	Using JavaScript and HTML for front-end development, as well as Leaflet library and other tools to create visual representation of our data and results.

•	Users will be able to input information (e.g. Country they choose to travel to)

• 	Once the user has entered the departure or destination countries, the website will generate when herd immunity will be reached in those countries in 	accordance with our machine learning model. 

•	The website will also generate a list of flights based on the departure/return date.

•	Users will be notified of travel advisories and whether it is safe to travel to that country. 

•	Website will include graphs that reflect COVID-19 vaccination data (percentage of individuals that are fully vaccinated)

•	Website Template: https://whimsical.com/covid-19-Wt8H3eaXMasUUiv68tSpT7 


-	The website will also generate a list of flights based on the departure/return date.

-	Users will be notified of travel advisories and whether it is safe to travel to that country. 

-	The user will be able to view further details of how herd immunity was calculate through a graph that reflects COVID-19 vaccination data (percentage of individuals that are fully vaccinated)

-	Website Template: https://whimsical.com/covid-19-Wt8H3eaXMasUUiv68tSpT7 

## Machine Learning Model 
 


-	During the initial investigation of the dataset, the interval between date entries are not consistent, some are updated daily and some are updated less frequently; this resulted in plenty of missing value. To mitigate the problem that would fit best the Arima model, the empty rows are filled using the pivot and melt method. With this method, all the countries would have the same number of entries starting at the original point
of December 19th, 2020. In addition, there are extra inputs on the location that arer aggregations of a number of countries. For example, 'world' is added to aggregate the world data. Therefore these entries are dropped.

-	Initial features for the model include:
	- location
	- date
	- people_vaccinated
	- people_fully_vaccinated
	- population
	- population_density
	- gdp_per_capita

- The model of choice is the Autoregressive Integrated Moving Average (ARIMA) model due to the time series nature of the data and the problem. However, the model has its limitations especially for long term forecasting. Since the model puts more weight on its most recent past data, there will be a time that the model will be forecasting based off of its own forecast thus creating a higher margin of error.

## Database: 
SQLite
- Script.py is uploaded in the github. It is a script for the database tables using sqllite. 
- Covid19_projection_db file is uploaded in github. We will be using SQLAlchemy.

=======
## Project: Interactive website for Post COVID-19 Vacation Planner

-	Using JavaScript and HTML for front-end development, as well as Leaflet library and other tools to create visual representation of our data and results.

-	Users will be able to input information (e.g. Country they choose to travel to)

- 	Once the user has entered the departure and destination country, the website will generate when herd immunity will be reached in those countries in accordance with our machine learning model. 

-	The website will also generate a list of flights based on the departure/return date.

-	Users will be notified of travel advisories and whether it is safe to travel to that country. 

-	The user will be able to view further details of how herd immunity was calculate through a graph that reflects COVID-19 vaccination data (percentage of individuals that are fully vaccinated)

-	Website Template: https://whimsical.com/covid-19-Wt8H3eaXMasUUiv68tSpT7 

## Machine Learning Model 
 


-	During the initial investigation of the dataset, the interval between date entries are not consistent, some are updated daily and some are updated less frequently; this resulted in plenty of missing value. To mitigate the problem that would fit best the Arima model, the empty rows are filled using the pivot and melt method. With this method, all the countries would have the same number of entries starting at the original point
of December 19th, 2020. In addition, there are extra inputs on the location that arer aggregations of a number of countries. For example, 'world' is added to aggregate the world data. Therefore these entries are dropped.

-	Initial features for the model include:
	- location
	- date
	- people_vaccinated
	- people_fully_vaccinated
	- population
	- population_density
	- gdp_per_capita

- The model of choice is the Autoregressive Integrated Moving Average (ARIMA) model due to the time series nature of the data and the problem. However, the model has its limitations especially for long term forecasting. Since the model puts more weight on its most recent past data, there will be a time that the model will be forecasting based off of its own forecast thus creating a higher margin of error.

## Database: 
SQLite
- Script.py is uploaded in the github. It is a script for the database tables using sqllite. 
- Covid19_projection_db file is uploaded in github. We will be using SQLAlchemy.

>>>>>>> 1241460bd01f1a3119d20762a6008bc4b52acd7c

