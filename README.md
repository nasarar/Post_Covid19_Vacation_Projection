# Post_COVID-19_Vacation_Projection 

## Selected topic

•	Help travellers plan their next vacation by determining when countries will reach herd immunity based on their current vaccination rate. 

## Reason we selected the topic: 

•	COVID-19 has impacted many people around the world and many people are eager to travel. A major barrier to travelling right now is safety. Based on the current vaccination rates in each country we are going to determine when each country will reach herd immunity. Herd immunity is reached when approximately 70% of the population is fully vaccinated. 

## Description of the source of data: 

- Data is being used from Our World in Data for all countries but firstly to test our model, we will be using 3 countries. 
- Website: https://ourworldindata.org/covid-vaccinations

Mathieu, E., Ritchie, H., Ortiz-Ospina, E. et al. A global database of COVID-19 vaccinations. Nat Hum Behav (2021). https://doi.org/10.1038/s41562-021-01122-8

## Questions we hope to answer with the data

## Defining the problem we plan to solve.
•	When will countries reach herd immunity for safe travelling? 

## Project: Interactive website for Post COVID-19 Vacation Planner

•	Using JavaScript for front-end development, as well as Leaflet library and other tools to create visual representation of our data and results.

•	Users will be able to input information (e.g. Country they chose to travel to)

• 	Once the user has entered the departure or destination countries, the website will generate when herd immunity will be reached in those countries in 	accordance with our machine learning model. 

•	The website will also generate a list of flights based on the departure/return date.

•	Users will be notified of travel advisories and whether it is safe to travel to that country. 

•	Website will include graphs that reflect COVID-19 vaccination data (percentage of individuals that are fully vaccinated)

•	Website Template: https://whimsical.com/covid-19-Wt8H3eaXMasUUiv68tSpT7 

### 1.2.0 Key Queries for Planner 
#### 1.2.1 Safe Vacation country identifier: 

-	Safe vacation country identifier would be a country that has reached herd immunity. 

#### 1.2.2 Hot spots identifier around the world

-	We will test our model on countries that are doing well with their vaccination efforts. The United States, Israel and United Kingdom will be used. 
	
#### 1.2.3 Status update for top 10 high frequency frequently visited vacation spots

###### Link : https://caen-keepexploring.canada.travel/things-to-do/10-surprising-places-ontario

##### 1.2.4 Fully vaccinated population status: 

We will be using the website mentioned (https://ourworldindata.org/covid-vaccinations) 

##### 1.2.5 Top 100 hotels, airbnb with 4* and 5* reviews for upkeeping covid safety protocols.

##### 1.2.6 Direct flights availability from one destination to another. (Find an API- Goodluck)
###### https://aviationstack.com/quickstart
        

###### Sample Model: US, Isreal, UK 

###### Data Storage: Postgres

##### ML Model: 
Time Series Regression Model
-	We will be using regression model for time series data to predict when 70% of the population will be fully vaccinated, hence achieving herd immunity. 
-	We will be able to answer this question and predict a future response based on past trends and observational data, given that vaccination is a continuous variable 
##### Database: 
SQLite

##### 2.1.0 Second Segment: Build the Pieces: Train your model and build out the database you will use for your final presentation.

##### 2.1.1 Data Gathering 
#####  2.1.2 Data pre-processing- Amandah
######  Python- Clean, prepare, explore
###### Libraries – Python and Javascript 
###### Tableau, Leaflet, Mapping– To visualize – Maneet and Zaineb 
#####2.1.3 Researching the model that will be best for the type of data- Ryan
#####2.1.4 Training and testing the model- Everyone (Testing the 3 countries only first)
##### 2.1.5 Evaluation- Everyone (Testing the 3 countries only) 

##### 3.1.0 Third Segment: Plug It In: 
##### 4.1.0 Fourth Segment: Put it all together

