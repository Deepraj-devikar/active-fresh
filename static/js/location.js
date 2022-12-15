// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.
let map, infoWindow;

function getLocation(){
    infoWindow = new google.maps.InfoWindow();
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          };
          infoWindow.setPosition(pos);
          infoWindow.setContent("Location found.");
          console.log(pos.lat);
          console.log(pos.lng);
          console.log(position);
        
        document.getElementById('lat').value = pos.lat;
        document.getElementById('lon').value = pos.lng;

        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;
 

        var geocoder = new google.maps.Geocoder();
        var latLng = new google.maps.LatLng(latitude, longitude);

        if (geocoder) {
            geocoder.geocode({ 'latLng': latLng}, function (results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                console.log(results[0].formatted_address); 
                document.getElementById('searchInput').value = results[0].formatted_address;
                console.log(results);
                place = results[0];
                console.log("state : "+place.address_components[5].long_name);
                document.getElementById('state').value = place.address_components[5].long_name;
                console.log("city : "+place.address_components[4].long_name);
                document.getElementById('city').value = place.address_components[4].long_name
            }
            else {
                console.log("Geocoding failed: " + status);
            }
            }); //geocoder.geocode()
        }
        },
      );
    } else {
    }
  }

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  );
  infoWindow.open(map);
}