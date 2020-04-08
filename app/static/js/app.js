let nextButton = document.getElementById('next-button');
let scaleElement = document.getElementById('scale');

nextButton.addEventListener('click', function (event) {
	$.getJSON('generate_one_scale', function (json) {
		var scale = JSON.parse(json);
		scaleElement.innerHTML = scale;
	});
});