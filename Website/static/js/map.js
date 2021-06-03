// Creating the map where airport locations will go 
// Accessing the airport data
let airportDataURL = "http://api.aviationstack.com/v1/airports?access_key=8d32007474ce2f1184533cb9ce09c196";

let map;
let streets;
let destinationSelector;
let departureSelector;
let locations = [];
let popup;

let destinationIndex = 0;
let departureIndex = 0;

function init_map(){
  map = L.map("mapid", {
    center: [0,0],
    zoom: 2
  });

streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
attribution: 'Map data © <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
  accessToken: API_KEY
});

  streets.addTo(map);
}

function init_dropdowns() {
  // Grab a reference to the dropdown select element
  destinationSelector = d3.select("#destinations");
  departureSelector = d3.select("#departures");
  let existing_countries = []
  d3.json(airportDataURL).then((data) => { // need to figure out how to get ALL the data
    console.log('Data: ', data);
    data.data.forEach((location) => {
      if (location.country_name && !existing_countries.includes(location.country_name)){ //getting rid of nulls and duplicates
        existing_countries.push(location.country_name);
        destinationSelector
          .append("option")
          .text(location.country_name)
          .property("value", locations.length);
        departureSelector
          .append("option")
          .text(location.country_name)
          .property("value", locations.length);
        locations.push(location);
      }
    });
  });
}

function set_popup_location(index){  // need to figure out how to get all the airports in that country and not just one
  let lat = locations[index].latitude;
  let lng = locations[index].longitude;
  popup = L.popup()
    .setLatLng([lat, lng])
    .setContent(`<p>Country name: ${locations[index].country_name}<br> Airport name: ${locations[index].airport_name}.</p>`)
    .openOn(map);
}

function destinationChanged(value){
  destinationIndex = value;
  set_popup_location(value);
}

function departureChanged(value){
  departureIndex = value;
  set_popup_location(value);
}
  