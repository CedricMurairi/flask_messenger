// alert('Hello I am here for you sir');
document.addEventListener('DOMContentLoaded', () => {

	// var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
	// document.querySelector('#sending-button').onclick = ()=>{
	// 	alert('message sent');
	// 	var message = document.querySelector('#message').value;
	// 	// socket.emit('send message', {'message': message});
	// }

	// socket.on('connect', ()=>{
	// 	document.querySelector('#sending-button').onclick = ()=>{
	// 		alert('message sent');
	// 		var message = document.querySelector('#message').value;
	// 		socket.emit('send message', {'message': message});
	// 	}
	// });

	// socket.on('recieve message', data =>{
	// 	const p = document.createElement('p');
	// 	const message = data.selection;
	// 	p.innerHTML = message;
	// 	document.querySelector('#message-area').append(p);
	// });

	document.getElementById('signin').addEventListener('click', function () {
		document.querySelector('#login-block').style.display = "block";
		document.querySelector('#registration-block').style.display = "none";
		document.querySelector('#contact-info').style.display = "none";
		document.querySelector('#message-area').style.display = "none";
	}, true);

	document.getElementById('register').addEventListener('click', function () {
		document.querySelector('#login-block').style.display = "none";
		document.querySelector('#registration-block').style.display = "block";
		document.querySelector('#contact-info').style.display = "none";
		document.querySelector('#message-area').style.display = "none";
	}, true);

	document.querySelector('#login-form').onsubmit = () => {
		alert('signin-form submitted');
		const user_email = document.querySelector("#log-email").value;
		const user_password = document.querySelector("#log-password").value

		var input = {
			email: user_email,
			password: user_password
		}

		fetch(`${window.origin}/login_user`, {
			method: 'POST',
			credentials: "include",
			body: JSON.stringify(input),
			cache: "no-cache",
			headers: new Headers({
				"content-type": "application/json"
			})
		}).then(function (response) {
			if (response.status !== 200) {
				console.log(`There ha been an error with the data ${response.status}`);
				return;
			}

			response.json().then(function (data) {
				if (data.login == true) {
					document.title = 'app';
					history.pushState(null, 'app', 'app');
					console.log(data);
					const displayName = data.result[1];
					const email = data.result.email;
					const userCard = document.querySelector("#user-name");
					document.querySelector("#signin").style.display = "none";
					document.querySelector("#register").style.display = "none";
					document.querySelector("#login-block").style.display = "none";
					document.querySelector("#registration-block").style.display = "none";
					document.querySelector("#logout").style.display = "inline-block";
					userCard.style.display = "inline-block";
					userCard.innerHTML = `${displayName}`
					document.querySelector('#contact-info').style.display = "block";
					document.querySelector('#message-area').style.display = "block";
				}

				else {
					console.log(data);
					const errorMessage = document.createElement('h4').innerHTML = `Error ${data.error}`;
					document.querySelector("#login-block").append(errorMessage);
				}
			});
		})

		return false;
	}

	document.querySelector('#reg-email').onkeyup = () => {
		const validEmailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
		if (document.querySelector('#reg-email').value.match(validEmailFormat)) {
			document.querySelector('#correct-email-error').style.color = "green";
		}
		else {
			document.querySelector('#correct-email-error').style.color = "red";
		}
	}

	document.querySelector('#reg-password').onkeyup = () => {
		const validPasswordFormat = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,25}$/;
		if (document.querySelector('#reg-password').value.match(validPasswordFormat)) {
			document.querySelector('#correct-password-error').style.color = "green";
		}
		else {
			document.querySelector('#correct-password-error').style.color = "red";
		}
	}

	document.querySelector('#reg-password-repeat').onkeyup = () => {
		if (document.querySelector("#reg-password").value == document.querySelector('#reg-password-repeat').value) {
			document.querySelector('#password-match-error').style.color = "green";
		}
		else {
			document.querySelector('#password-match-error').style.color = "red";
		}
	}

	document.querySelector('#logout').onclick = () => {
		fetch(`${window.origin}/logout`, {
			method: 'POST',
			credentials: "omit",
			body: null,
			cache: "no-cache",
			headers: new Headers({
				"context-type": "application/json"
			})
		}).then(function (response) {
			if (response.status !== 200) {
				console.log("Domething went wrong with logout");
				return;
			}
			response.json().then(function (data) {
				if (data.logout == true) {
					console.log(data);
				}
			})
		})
	}

	document.querySelector('#registration-form').onsubmit = () => {
		alert('registration-form submitted');
		// const request = new XMLHttpRequest();
		const user_name = document.querySelector("#reg-name").value;
		const user_email = document.querySelector("#reg-email").value;
		const user_password = document.querySelector("#reg-password").value;

		// request.open('POST', `${window.origin}/register`);

		var input = {
			name: user_name,
			email: user_email,
			password: user_password
		}

		fetch(`${window.origin}/register_user`, {
			method: 'POST',
			credentials: "include",
			body: JSON.stringify(input),
			cache: "no-cache",
			headers: new Headers({
				"content-type": "application/json"
			})
		}).then(function (response) {
			if (response.status !== 200) {
				console.log(`There ha been an error with the data ${response.status}`);
				return;
			}

			response.json().then(function (data) {
				if (data.registered == true) {
					document.title = 'app';
					history.pushState(null, 'app', 'app');
					const displayName = user_name;
					// const user_email = user_email;
					const userCard = document.querySelector("#user-name");
					document.querySelector("#signin").style.display = "none";
					document.querySelector("#register").style.display = "none";
					document.querySelector("#login-block").style.display = "none";
					document.querySelector("#registration-block").style.display = "none"
					document.querySelector("#logout").style.display = "inline-block";
					userCard.style.display = "inline-block";
					userCard.innerHTML = `${displayName}`
					document.querySelector('#contact-info').style.display = "block";
					document.querySelector('#message-area').style.display = "block";
				}

				else {
					const errorMessage = document.createElement('h4').innerHTML = `Error ${data.error}`;
					document.querySelector("#registration-block").append(errorMessage);
				}
			});
		})

		// console.log('open request');

		// request.onload = () => {
		// 	console.log(request.status);
		// 	const data = JSON.parse(request.responseXML);

		// 	console.log('data recieved');
		// 	console.log(data);

		// 	if (data.registered == true) {
		// 		const displayName = name;
		// 		const user_email = email;
		// 		document.querySelector("#signin").style.display = "none";
		// 		document.querySelector("#register").style.display = "none";
		// 		const signout = document.createElement("li").className = "button";
		// 		document.querySelector("#buttons").append(signout);
		// 	}

		// 	else {
		// 		const errorMessage = document.createElement('h4').innerHTML = `Error ${data.error}`;
		// 		document.querySelector("#registration-block").append(errorMessage);
		// 	}
		// };

		// const data = new FormData();
		// var input = {
		// 	'name': name,
		// 	'email': email,
		// 	'password': password
		// }
		// data.append(input);

		// request.send(data);
		// console.log('data sent');
		return false;
	}
});


