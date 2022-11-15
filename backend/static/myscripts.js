var base_url = "http://localhost:5000" // Ewww...
var xhr = null;
getXmlHttpRequestObject = function () {
	if (!xhr) {
		xhr = new XMLHttpRequest();
	}
	return xhr;
};

function dataCallback() {
	if (xhr.readyState == 4 && xhr.status == 200) {
		console.log("We have news");
		dataDiv = document.getElementById('result-container');
		dataDiv.innerHTML = xhr.responseText;
	}
};

function lobbyFunction() {
	var request_url = "/lobby"
	console.log("Show the welcome message onload")
	xhr = getXmlHttpRequestObject();
	xhr.onreadystatechange = dataCallback;
	xhr.open("GET", base_url+request_url, true);
	xhr.send(null);
};

try {
	const form = document.getElementById("myForm");
	if (form != null){
		form.addEventListener("submit", (event) => {
			event.preventDefault();
			
			const formData = new FormData(form)
			var request_url = "/greet"
			console.log("I am thinking I should say hello")
			xhr = getXmlHttpRequestObject();
			xhr.onreadystatechange = dataCallback;
			xhr.open("POST", base_url+request_url, true);
			xhr.send(formData);

		});
	}
}
catch (TypeError) {
	console.log(TypeError)
}
try {
	var dropZone = document.getElementById('drop_zone');
	if (dropZone != null) {
		dropZone.addEventListener('dragover', function(e) {
			e.stopPropagation();
			e.preventDefault();
		});

		// Get file data on drop
		dropZone.addEventListener('drop', function(e) {
			e.stopPropagation();
			e.preventDefault();
			var file = e.dataTransfer.files[0]
			console.log(file)
			file_upload_form = new FormData()
			file_upload_form.append('file', file, file.name)
			var request_url = "/upload"
			xhr = getXmlHttpRequestObject();
			xhr.onreadystatechange = dataCallback;
			xhr.open("POST", base_url+request_url, true);
			xhr.send(file_upload_form);
		});
	}
}

catch (TypeError) {
	console.log(TypeError)
}