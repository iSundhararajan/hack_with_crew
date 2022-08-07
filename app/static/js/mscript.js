function Mapping() {
    var mapProp = { // map view begins zoomed out
      center: new google.maps.LatLng(0, 0),
      zoom: 3,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
    for (let i = 0; i < countries.length; i++) { 
      var marker = new google.maps.Marker({ // add a marker for each country visited
          position: new google.maps.LatLng(countries[i].lat, countries[i].long),
          map: map
      });
      addInfoWindow(marker, "content");
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