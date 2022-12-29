function initMap() {
    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer()
    const location = { lat:  -7.11532, lng: -34.861 }; 
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 14,
      center: location,
    });
  
    const geocoder = new google.maps.Geocoder();
    var position_of_the_destiny = document.getElementById('ed').value
    geocoder
    .geocode({address: position_of_the_destiny, region: 'BR'})
    .then((response) => {
      const destiny_position = response.results[0].geometry.location;
      let marker = new google.maps.Marker({
      position: destiny_position,
      map,
      title: "Hello World!",
    });
    })
  
  
    directionsRenderer.setMap(map);
  
    const onChangeHandler = function () {
      calculateAndDisplayRoute(directionsService, directionsRenderer);
    };
    onChangeHandler()
  
    map.addListener("zoom_changed", () => {
      window.setTimeout(() => {
        map.setZoom(13);
      }, 15000);
    });
    }
  
  function calculateAndDisplayRoute(directionsService, directionsRenderer) {
  function success(pos) {
    const crd = pos.coords;
    var position_of_the_user =  crd.latitude + ', ' + crd.longitude
    var position_of_the_destiny = document.getElementById('ed').value
    
    directionsService
    .route({
      origin: {
          query: position_of_the_user
      },
      destination: {
         query: position_of_the_destiny
      },
      travelMode: google.maps.TravelMode.DRIVING,
    })
    .then((response) => {
      directionsRenderer.setDirections(response);
    })
    .catch((e) => window.alert("Directions request failed due to " + e)); 
  }
  
  const position_check = navigator.geolocation.getCurrentPosition(success);
   
  }
  
  window.initMap = initMap;


  document.getElementById('maps-btn').addEventListener('click', () => {
    var daddr = window.location.search.slice(1);
    var position_of_the_destiny = document.getElementById('ed').value
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(data){
      if (data.coords) {
        window.open(`https://maps.google.fr/maps?saddr=${data.coords.latitude},${data.coords.longitude}&daddr=${daddr}/${position_of_the_destiny}`, '_blank') 
      }
      });
    }
})