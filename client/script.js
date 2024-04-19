
const map = L.map('map').fitWorld();

const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

function onLocationFound(e) {
  const radius = e.accuracy / 2;

  const locationMarker = L.marker(e.latlng).addTo(map)
    .bindPopup(`You are within ${radius} meters from this point`).openPopup();

  const locationCircle = L.circle(e.latlng, radius).addTo(map);
}

function onLocationError(e) {
  alert(e.message);
}

map.on('locationfound', onLocationFound);
map.on('locationerror', onLocationError);

map.on("click", function(e){
  var marker = new L.marker([e.latlng.lat, e.latlng.lng]).addTo(map);
  console.log(marker);
  console.log(e);
  let data = {
    srid: 3857,
    lat: e.latlng.lat,
    lng: e.latlng.lng
  }
  savePoint(data);
})

function savePoint(data) {
  var jsonData = data;

  fetch('http://localhost:5000/receive_data', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(jsonData),
  })
  .then(response => response.text())
  .then(data => {
      console.log('Success:', data);
      alert('Data sent successfully');
  })
  .catch((error) => {
      console.error('Error:', error);
      alert('Failed to send data');
  });
}

map.locate({setView: true, maxZoom: 16});