/* jshint devel:true */
var map;
var locations = {
	'shibuya': [35.6585, 139.7013],
	'shinjuku': [35.6938, 139.7036]
}

function initializeMap() {
	var mapOptions = {
		zoom: 15,
		center: new google.maps.LatLng(locations.shibuya[0], locations.shibuya[1])
	};
	map = new google.maps.Map($("#map-canvas")[0],
		mapOptions);
}

function moveLocation(sel) {
	map.panTo(new google.maps.LatLng(locations[sel.value][0], locations[sel.value][1]));
}

google.maps.event.addDomListener(window, 'load', initializeMap);

