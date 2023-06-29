function iniciarMap(){
    var coord ={lat:-33.51694393265615, lng:-70.75625188507036};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 10,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map

    })
}

