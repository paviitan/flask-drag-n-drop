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

function greetFunction() {
	var request_url = "/greet"
	console.log("I am thinking I should say hello")
	xhr = getXmlHttpRequestObject();
	xhr.onreadystatechange = dataCallback;
	xhr.open("GET", base_url+request_url, true);
	xhr.send(null);
}