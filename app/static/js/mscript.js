function initMap() {
    var mapProp = { // map view begins zoomed out
      center: new google.maps.LatLng(46.3333, -63.5000),
      zoom: 4,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
    for (let i = 0; i < places.length; i++) {
        geocode(places[i][0], ({ lat, long }) => {
            var marker = new google.maps.Marker({ // add a marker for each country visited
                position: new google.maps.LatLng(lat, long),
                map: map
            });
            const content = '<div id="content">' +
            '<div id="siteNotice">' +
            "</div>" +
            '<h1 id="firstHeading" class="firstHeading">'+ places[i][1] +'</h1>' +
            '<div id="bodyContent">' +
            "<h4>Location: " + places[i][0] +'</h4>' +
            "<h4>Date: " + places[i][2] +'</h4>' +
            '<h4>More information: <a href="'+ places[i][3] + '">Take me to their website!</a>' +
            "</h4>" +
            "</div>" +
            "</div>"
            addInfoWindow(marker, content);
        })
    }

    function addInfoWindow(marker, message) {
        var infoWindow = new google.maps.InfoWindow({
            content: message
        });

        google.maps.event.addListener(marker, 'click', function () {
            infoWindow.open(map, marker);
        });
    }
}

// find long and lat coordinates of locations
function geocode(place, callback){
    axios.get('https://maps.googleapis.com/maps/api/geocode/json',{
        params:{
            address: place,
            key: API_KEY,
        }
    })
    .then(function(response){
        // Log full response
        console.log(response);

        // long and lat
        var lati = response.data.results[0].geometry.location.lat;
        var longit = response.data.results[0].geometry.location.lng;
        callback({
            lat: lati,
            long: longit
        });
    })
    .catch(function(error){
        console.log(error);
    });
}