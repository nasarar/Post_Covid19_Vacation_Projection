function init() {
    // Grab a reference to the dropdown select element
    var selector = d3.select("#selDataset");

    // Use the list of locations to populate the select options


      var locationNames = vaccinationData.map(x=> x.location);
      locationNames = [...new Set(locationNames)];
      locationNames.forEach((location) => {
        selector
          .append("option")
          .text(location)
          .property("value", location);
      });

      // Use the first location from the list to build the initial plots
      var firstLocation = locationNames[0];
      buildCharts(firstLocation);


  }

  // Initialize the dashboard
  init();

  function optionChanged(newLocation) {
    // Fetch new data each time a new location is selected
    buildCharts(newLocation);
  }

  function buildCharts(location) {
    // Use d3.json to load and retrieve the world_data_forecast.json file

      // Create a variable that filters the location for the object with the desired location
      var resultsArray = vaccinationData.filter(resultsObj => resultsObj.location == location && resultsObj.people_fully_vaccinated <71);
      // Create variables that hold the vaccinated and date.
      var date = resultsArray.map(x=> x.date_adjusted);
      var vaccinated = resultsArray.map(x=> x.people_fully_vaccinated);
      // Create the trace for the line chart.
      var scatterData = [{
        x: date,
        y: vaccinated,
        mode: 'lines',
        line: {
          color: 'rgb(0, 0, 0)',
          width: 2
        }
      }];
      // Create the layout for the bar chart.
       var scatterLayout = {
        title: {text: "Vaccination Rate for " + location},
        xaxis: {
          title: 'Date',
        },
        yaxis: {
          title: 'Percent Fully Vaccinated (%)',
          range: [0, 71]
        }
      };
      // Use Plotly to plot the data with the layout.
      Plotly.newPlot("line", scatterData, scatterLayout);

  }
