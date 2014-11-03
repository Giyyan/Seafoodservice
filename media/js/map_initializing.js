function initialize() {
    var myLatlng = new google.maps.LatLng(17.412856, 50.283015);
    var mapOptions = {
        zoom: 2,
        center: myLatlng,
        scrollwheel: false,
        navigationControl: false,
        mapTypeControl: false,
        scaleControl: false,
        draggable: false
    }
    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    var points = $('#transporation_points').children().toArray();

    var infoWindow = new google.maps.InfoWindow({
        content: 'myContent'
    });
    var shape = {
        coord: [1, 1, 1, 20, 18, 20, 18 , 1],
        type: 'poly'
    };
    var image = new google.maps.MarkerImage('/media/css/images/google_map_point.png');
    var markers = new Array();
    var infoWindows = new Array();
    for (var i = 0; i < points.length; i++) {
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(parseFloat($('#latitude_' + i).text()), parseFloat($('#longitude_' + i).text())),
            map: map,
            title: $('#title_' + i).text(),
            zIndex: i,
            icon: image
        });
        marker.info = new google.maps.InfoWindow({
            content: '<p style="color: red;">' + $('#title_' + i).text()+'</p><a style="margin:3%;">' + $('#description_' + i).text()+'</a>'
        });
        google.maps.event.addListener(marker, 'click', function () {
            this.info.open(map, this);
        });
        markers.push(marker);
    }

    var styler = [
        {
            "featureType": "administrative",
            "elementType": "geometry",
            "stylers": [
                { "visibility": "on" },
                { "color": "#c6c5c3" }
            ]
        },
        {
            "featureType": "road",
            "elementType": "labels",
            "stylers": [
                { "visibility": "on" },
                { "color": "#c6c5c5" }
            ]
        },
        {
            "featureType": "landscape.natural",
            "stylers": [
                { "visibility": "on" },
                { "color": "#c9c6c5" }
            ]
        },
        {
            "featureType": "water",
            "elementType": "geometry",
            "stylers": [
                { "visibility": "on" },
                { "color": "#f2f2f2" }
            ]
        },
        {
            "featureType": "water",
            "elementType": "labels",
            "stylers": [
                { "visibility": "off" }
            ]
        },
        {
            "featureType": "administrative",
            "elementType": "labels",
            "stylers": [
                { "visibility": "off" }
            ]
        },
        {
        }
    ]
    map.setOptions({styles: styler});
}