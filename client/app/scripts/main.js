/* jshint devel:true */
var map;
var locations = {
	'shibuya': [35.6585, 139.7013],
	'shinjuku': [35.6938, 139.7036]
};
var data;

function initializeMap() {
	var mapOptions = {
		zoom: 15,
		center: new google.maps.LatLng(locations.shibuya[0], locations.shibuya[1])
	};
	map = new google.maps.Map($("#map-canvas")[0],
		mapOptions);
	setTimeout(function () {
		data.hits.hits.forEach(function (hit) {
			var tmp = hit._source.geo;
			var myLatlng = new google.maps.LatLng(tmp[0], tmp[1]);
			var marker = new google.maps.Marker({
				position: myLatlng,
				map: map,
				title: "Hello World!"
			});
			google.maps.event.addListener(marker, 'click', function () {
				$("#place-img").html("<img src='" + hit._source.reference_picture + "' height='80' width='80'>");
				$("#place-desc").text(hit._source.name);
				$("#place-reason").text(hit._source.reason);
			});
		});
	}, 1000);
}

function moveLocation(sel) {
	map.panTo(new google.maps.LatLng(locations[sel.value][0], locations[sel.value][1]));
}

google.maps.event.addDomListener(window, 'load', initializeMap);

var es = new $.es.Client({
	host: {
		host: '52.4.196.153',
		port: '9200'
	}
});

es.search({
	index: 'ep_venues',
	type: 'venue'
}, function (error, response) {
	data = response;
});