function Mapping() {
    var mapProp = { // map view begins zoomed out
      center: new google.maps.LatLng(0, 0),
      zoom: 3,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
    for (let i = 0; i < places.length; i++) {
        geocode(places[i], ({ lat, long }) => {
            var marker = new google.maps.Marker({ // add a marker for each country visited
                position: new google.maps.LatLng(lat, long),
                map: map
            });
            addInfoWindow(marker, "content");
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