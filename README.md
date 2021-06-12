
<img width="1167" alt="Screen Shot 2021-06-08 at 11 34 40 PM" src="https://user-images.githubusercontent.com/75267605/121289415-e95f4180-c8b2-11eb-94e8-6fccbff9f3dc.png">




## Presentation 
#### **The presentation for the project can be accessed [here](https://docs.google.com/presentation/d/10SREyI6aJZHYDQQToGYDDiN4IGymO-KeN4DXxd2qc8g/edit#slide=id.gdd6f86eaab_0_138)** 
 
#### **The jupyter notebook for the Machine Learning model can be accessed  [here](https://github.com/nasarar/Post_Covid19_Vacation_Projection/blob/main/pcvplanner.ipynb).**


## Purpose 



The project aims to identify and forecast countries that will reach herd immunity by inducing the Arima model on the updated covid fully vaccinated data from our world. The model will evaluate and forecast the future data based on the past and present vaccination rate.

The herd immunity is reached when 70% of the population are fully vaccinated with both the doses.

The people planning to travel in the near future can visit the website ............. and check for a future date for travel to a particular destination, and the model will help them to know the countries that will reach herd immunity and will mark it as safe for travel.

The model can also be fine-tuned for NGOs to know which countries will need help in reaching the herd immunity by providing the details of the earliest date and year by which a particular country can be marked safe for travel. 

NGO's directed by WHO/UN can then send a team with vaccinations and mobile medical unit to vaccinate countries/state who will be ready for such assistance.


## Tools and Tech Used 
<img width="1068" alt="Screen Shot 2021-06-12 at 10 25 09 AM" src="https://user-images.githubusercontent.com/75267605/121779203-872f6680-cb68-11eb-9c95-f4406a5805d5.png">




## Data Analysis Phase
- Data is being used from Our World in Data for all countries but firstly to test our model, we will be using 3 countries. 
- Website: https://ourworldindata.org/covid-vaccinations
- Ourwordlin data is dependent on the data of vaccination fed in by the countries medical bodies similar to cdc of USA 
- Some countries like Afghanistan approach in feeding data is not consistent like many more and 
- The countries approachto vacinations differ based on the availability of vaccinations in different countries.
- Canada approached vaccination by keeping a lag of 3-4 months bewteen two doses in order to provide minimum protection of one dose to all.
- checked statistical validity of ourworldin data
- checked for the nulls,verfied and deleted as required
- checked the datatypes and removed wrong datatype values and re-transformed datatypes
- dropped,deleted  or excluded irrelevant columns
- visualized our data for our need 
- binned data whereever appropriate
- checked all the columns for unique values
- split the data into training and testing datasets
- created calculated conditions for our scripts for machine learning model
- supervised and unsupervised learning, dimensionality reduction
- rescaling data




## Machine Learning Model


### Block Diagram of Arima Model 

<img width="935" alt="Screen Shot 2021-06-08 at 12 42 05 AM" src="https://user-images.githubusercontent.com/75267605/121126045-85c30e80-c7f5-11eb-9214-e7ba7248c56c.png">


-During the initial investigation of the dataset, it was evaluated that the interval between date entries are not consistent, as some are updated daily and some are updated less frequently; this resulted in plenty of missing value. 
-To mitigate the problem that would fit best the Arima model, the empty rows are filled using the pivot and melt method. With this method, all the countries would have the same number of entries starting at the original point of December 19th, 2020. 
-In addition, there are extra inputs on the location that are aggregations of a number of countries. For example, 'world' is added to aggregate the world data. Therefore these entries are dropped.

-	Initial features for the model include:
	- location
	- date
	- people_vaccinated
	- people_fully_vaccinated
	- population
	- population_density
	- gdp_per_capita

- The model of choice is the Autoregressive Integrated Moving Average (ARIMA) model due to the time series nature of the data and the problem. However, the model has its limitations especially for long term forecasting. Since the model puts more weight on its most recent past data, there will be a time that the model will be forecasting based off of its own forecast thus creating a higher margin of error.
- The Arima Model we have worked out for the data works best with p,d,q value of 7,0,0. 
- For loop is used to 
- Checked stationarity: Time series has to be independent of trend or seasonality component before we can use ARIMA to forecast.
- Difference: The time is made stationarized through differencing. We were able to utilize two differening to make the series stationary.
- Filter out a validation sample: This will be used to validate how accurate our model is. We Used train test validation split to achieve this.
- Select AR and MA terms: Use the ACF and PACF to decide whether to include an AR term(s), MA term(s), or both.We settled on P & Q to be at 4 to get the best results 
- Build the model: Build the model and set the number of periods to forecast to N (12*30 days).
- Validate the model: Compare the predicted values to the actuals in the validation sample.


- Read cleaned data

<img width="831" alt="step1-read the data " src="https://user-images.githubusercontent.com/75267605/121627140-cf556880-ca44-11eb-8086-61641ffd0beb.png">


- Resampled the cleaned data



<img width="629" alt="resample1" src="https://user-images.githubusercontent.com/75267605/121627200-eb590a00-ca44-11eb-883c-cc074ea100c9.png">

<img width="654" alt="reseample 2" src="https://user-images.githubusercontent.com/75267605/121627227-f6ac3580-ca44-11eb-8121-d57684996740.png">


- Stationarity check on resampled data 



<img width="730" alt="stationarity check " src="https://user-images.githubusercontent.com/75267605/121627304-17748b00-ca45-11eb-9ac5-d7380c4bdd94.png">


- Data split for Train & test 

<img width="485" alt="Train   Test " src="https://user-images.githubusercontent.com/75267605/121627451-602c4400-ca45-11eb-98e9-7e5ac90d86c6.png">




- Build ARIMA model and determine Hyperparameters of the model


<img width="578" alt="RMSE train   Test" src="https://user-images.githubusercontent.com/75267605/121627672-cb761600-ca45-11eb-9ce1-a11fed9b4fc5.png">


<img width="560" alt="Armia model pdq value " src="https://user-images.githubusercontent.com/75267605/121627684-d29d2400-ca45-11eb-8bae-155cf03f1ef9.png">


- Predict Data set 




<img width="681" alt="predict data set " src="https://user-images.githubusercontent.com/75267605/121627982-64a52c80-ca46-11eb-9e89-3b7e84e50aa2.png">


- Model Validation


<img width="602" alt="model validation 01" src="https://user-images.githubusercontent.com/75267605/121628102-9d450600-ca46-11eb-842a-4b25fcdbe0a6.png">



<img width="847" alt="model validation 02" src="https://user-images.githubusercontent.com/75267605/121628188-c49bd300-ca46-11eb-97eb-5fdb760be316.png">


- Predict Future data 


<img width="666" alt="predict future data " src="https://user-images.githubusercontent.com/75267605/121628344-03ca2400-ca47-11eb-9fcb-918cb1621652.png">


<img width="753" alt="predict future data 01" src="https://user-images.githubusercontent.com/75267605/121628399-22301f80-ca47-11eb-8225-bd485faed70f.png">





## Examples

- Four  countries CAN, USA, GBR and AUS  were identfied to generate the plots as examples for documentation.


### Plots and herd immunity prediction for CAN
#### **CAN**

<img width="654" alt="Best_Model_pdq_can" src="https://user-images.githubusercontent.com/75267605/121689549-b96e9480-ca92-11eb-8845-62093a76ded7.png">

<img width="794" alt="plot_can" src="https://user-images.githubusercontent.com/75267605/121689507-ad82d280-ca92-11eb-9ab6-2f796305ced1.png">


<img width="840" alt="fvr_can" src="https://user-images.githubusercontent.com/75267605/121689491-a8258800-ca92-11eb-822b-88f17a1c070b.png">



#### **Herd Immunity for Canada is predicted to be reached by 11th September 2021**


<img width="566" alt="herd_immunity_CAN" src="https://user-images.githubusercontent.com/75267605/121689677-e9b63300-ca92-11eb-81ac-6d17bdf31eab.png">



### Plots and herd immunity prediction for GBR


#### **GBR**

<img width="781" alt="plot_gbr" src="https://user-images.githubusercontent.com/75267605/121690302-af00ca80-ca93-11eb-802a-14f93e8e622f.png">

<img width="680" alt="best_model_gbr" src="https://user-images.githubusercontent.com/75267605/121690320-b45e1500-ca93-11eb-9ed1-31fb29d5efc5.png">

<img width="813" alt="fvr_gbr" src="https://user-images.githubusercontent.com/75267605/121690349-baec8c80-ca93-11eb-9e85-d1830b31d9c3.png">

#### **Herd Immunity for GBR is predicted to reach on 2nd October 2021**


<img width="591" alt="herd_immunity_GBR" src="https://user-images.githubusercontent.com/75267605/121690354-be801380-ca93-11eb-9ebf-29116ba0ac00.png">

### Plots and herd immunity prediction for USA

#### **USA**

<img width="771" alt="plot_usa" src="https://user-images.githubusercontent.com/75267605/121690577-056e0900-ca94-11eb-80c1-86da5c6da455.png">

<img width="626" alt="best_model_pdq_usa" src="https://user-images.githubusercontent.com/75267605/121690595-0a32bd00-ca94-11eb-9f11-f949e0b57178.png">

<img width="783" alt="fvr_usa" src="https://user-images.githubusercontent.com/75267605/121690609-0f900780-ca94-11eb-938e-bf722364ca93.png">


#### **Herd Immunity for USA is predicted to reach on 23rd September 2021**


<img width="564" alt="herd_immunity_USA" src="https://user-images.githubusercontent.com/75267605/121690619-13238e80-ca94-11eb-8811-44ae130b78b6.png">



### Plots and herd immunity prediction for AUS

#### **AUS**

<img width="768" alt="plot_Aus" src="https://user-images.githubusercontent.com/75267605/121690823-52ea7600-ca94-11eb-9538-b234059162f4.png">

<img width="630" alt="best_model_aus" src="https://user-images.githubusercontent.com/75267605/121690861-5b42b100-ca94-11eb-9bf6-78e199694b79.png">


<img width="778" alt="fvr_aus" src="https://user-images.githubusercontent.com/75267605/121690927-6f86ae00-ca94-11eb-9592-b679922bec49.png">

#### **Herd Immunity for AUS is predicted to reach on 29th October 2021**


<img width="551" alt="herd_immunity_AUS" src="https://user-images.githubusercontent.com/75267605/121690970-7b727000-ca94-11eb-885e-8b7515a3630a.png">






- 
## Database
### **SQLite**
- Script.py.ipynb is the script used to create the database in SQLite. Used pandas and python to query the database to create tables. Ran the jupyter notebook to test the code. 
- World_data_forecast.csv file and the json created is in the resources folder. 
- Used Flask to connect database to the web application.

## Website & Visualizations

Using JavaScript and HTML for front-end development, as well as Leaflet library and other tools to create visual representation of our data and results.

•	Users will be able to select a country from a dropdown list (e.g. departure or destination country)

• 	Once the user has selected the departure or destination country, the website will generate when herd immunity will be reached in that country in 	accordance with our machine learning model. 

•	An interactive map will include popup markers of airports in the chosen countries based on the aviationstack API (https://aviationstack.com/) 

<img src = "https://github.com/nasarar/Post_Covid19_Vacation_Projection/blob/955bc001563294e8d3cae6aaecf5981e2250d10d/map.png">

-	The website will also generate a list of nearby hotels (within 5 km) of the user's choice of location based on Google Places API. 

<img src = "https://github.com/nasarar/Post_Covid19_Vacation_Projection/blob/955bc001563294e8d3cae6aaecf5981e2250d10d/hotels.png">

-	The user will be able to view further details of how herd immunity was calculate through a graph that reflects COVID-19 vaccination data (percentage of individuals that are fully vaccinated)

-	Website Template: https://whimsical.com/covid-19-Wt8H3eaXMasUUiv68tSpT7 


## Demonstration 

### Post covid-19 vacation planner tab

- We can select departure and destination countries which in this case was USA and Brazil to showcase the herd immunity prediction dates and schedule of both countries,  which was 15th November 2021 and 31st Jan 2022. These informations will help the potential travellers to make  intelligent decisions to travel to those countries .

<img width="1276" alt="Screen Shot 2021-06-11 at 6 41 35 PM" src="https://user-images.githubusercontent.com/75267605/121755398-1430dc00-cae5-11eb-9cdd-d6ed0f2752ae.png">


- Pop up additionaly displayed the Airport travellers could possibly travel to based on their  travel plans 


<img width="1300" alt="Screen Shot 2021-06-11 at 6 42 33 PM" src="https://user-images.githubusercontent.com/75267605/121755408-18f59000-cae5-11eb-9594-0ebf1fc27055.png">

- When the airport name is typed in it provides a list of hotels to choose from.



<img width="1126" alt="Screen Shot 2021-06-11 at 6 43 17 PM" src="https://user-images.githubusercontent.com/75267605/121755421-1eeb7100-cae5-11eb-960b-1c0f201fe9c8.png">

### Covid 19 vaccination tab

#### Vaccination rate of USA, GBR and AUS

- **USA**


<img width="910" alt="VACCINATION RATE OF USA" src="https://user-images.githubusercontent.com/75267605/121765625-4c064680-cb1a-11eb-8028-1c5113758fa6.png">

- **GBR**

<img width="843" alt="VACCINATION RATE OF GBR" src="https://user-images.githubusercontent.com/75267605/121765627-4f013700-cb1a-11eb-9e09-d13d54442e50.png">

- **AUS**


<img width="889" alt="VACCINATION RATE OF AUS" src="https://user-images.githubusercontent.com/75267605/121765631-53c5eb00-cb1a-11eb-9229-304cf79678de.png">


# Summary of Analysis 

- The post covid19 travel planner is built on the Time series ARIMA model by identifying the right hyperparameters (p,d,q) for each countries.
- The Hyperparameters (p,d,q) range is identfied by for loop method wherein least RSME ( root square mean error) provides the highest range of hyperparameters(p,d,q).
- The Hyperparameters identfied for our data range and countries was 7,0,0
- We see a definte surge in the vaccination drive among countries who are manfacturing the vaccines.
- Countries like USA, UK (GBR), Russia, Israel are expected to reach herd immunity by fourth quarter of 2021.
- The webapp is designed to have its input from the prediction updated data daily in order to have an update herd immunity data for each country listed in the app.
- Sqllite data base is used for faster deployment with local access 
- Sqllite has its disadvantes of limitations with access and security features. 

# Recommendation for future analysis

- Regular daily update of data in the data pool will assist the model to provide better prediction process.
- Better and safe data base like AWS and postgress will help the mdoel to be more safe and rugged 
- The webapp and model can be better utlized for NGO's to assist and speed up vaccination process for countries which have delayed reach in its herd immunity.





