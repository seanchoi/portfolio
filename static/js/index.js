var map;
// search input works by key 'Enter'
document.getElementById("zip-code-input").onkeydown = function (event) {
    if (event.keyCode === 13) {
    search();
    }
};
var infoWindow;
var markers =[];
function initMap() {
    var RockvilleMD = {
        lat: 39.0839973, 
        lng: -77.1527578        
    }    
    map = new google.maps.Map(document.getElementById('map'), {
    center: RockvilleMD,
    zoom: 10,       
    });
    infoWindow = new google.maps.InfoWindow();
    search();    
}
// search by a given condition but if nothing is given show all the list and markers.
function search() {
    var foundStores = [];
    var searchQue = document.getElementById('zip-code-input').value; //get value from zip-code-input class 
    if(searchQue) { 
        stores.forEach(function(store){            
            var city = store.city;                                    
            var zipcode = store.zipcode;
            if (city.toLowerCase() == searchQue.toLowerCase() || zipcode === searchQue ) {
                foundStores.push(store);
            }        
        });
    } else { //if no condition is given at page loading, show all the stores
        foundStores = stores;
    };
    clearLocations() // once condition is given list will show only list by the condition so all the markers previously shown should be all removed
    displayLists(foundStores);
    showStoresMarkers(foundStores);
    setOnClickListener();
}
function clearLocations() { // clearing all markers currently showing on the map
    infoWindow.close();
    for (var i = 0; i < markers.length; i++) {
      markers[i].setMap(null);
    }
    markers.length = 0;  
}
//connect a list from left to designated marker by click
function setOnClickListener() {    
    var storeElements = document.querySelectorAll('.member-container'); //store-container represents a single list
    storeElements.forEach(function(elem, index) {
        elem.addEventListener('click', function(){
            google.maps.event.trigger(markers[index], 'click')
        });
    });
}
// diplay all lists from data 
function displayLists(stores) {
    var listHtml = "";    
    stores.forEach(function(store, index){     
        var list_name  = store.store_name;
        var address = store.addressLines;
        listHtml += `
            <div class="member-container">
                <div class="member-container-bg">
                    <div class="member-info-container">
                        <div class="member-address">
                            <span>${list_name}</span>
                            <span>${address[0]}</span> 
                            <span>${address[1]}</span> 
                        </div>                        
                    </div> 
                    <div class="list-num-container">
                        <div class="list-number-bg">
                            <div class="list-num">${index+1}</div>
                        </div>
                    </div>
                </div>                    
            </div>               
        `      
    });
    document.querySelector('.member-list').innerHTML = listHtml; // '.stores-list' target class name 
}
// MAPPING - showing markers 
function showStoresMarkers(stores) {
    var bounds = new google.maps.LatLngBounds(); //zoom the whole boundary to fit in the broswer window.   
    stores.forEach( function(store,index){       
        var latlng = new google.maps.LatLng(
            Number(store.coordinates.lat),
            Number(store.coordinates.lon));
        var name = store.store_name;
        var stAddress = store.address;
        var phone = store.phone;        
        var lat = Number(store.coordinates.lat); 
        var lon = Number(store.coordinates.lon);           
        bounds.extend(latlng);        
        createMarker(latlng, lat, lon, name, stAddress, phone, index);
    })
    map.fitBounds(bounds);
}