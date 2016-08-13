/* Clients custom carousel */
$.ajax({
	type: "POST",
	url: url,
  data: null,
	dataType: "json",
	success: callback,
});

$(document).ready(function() {
	$('.indicators a').click(function(event){

		$.getJSON('static/bower_components/bootstrap/dist/js/clients.json', function(data) {
			$('.media-body').append( $('media-body'));
			$('.media-heading').append( $('media-heading'));
			$('.media-desc').append( $('media-desc'));
		});
	});
});
