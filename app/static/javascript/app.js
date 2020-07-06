// alert('Hello I am here for you sir');
document.addEventListener('DOMContentLoaded', () => {

	var login_block = document.querySelector('#login-block');
	var registration_block = document.querySelector('#registration-block');
	var main_container = document.querySelector('#main-container');
	var signin_button = document.querySelector('#signin');
	var register_button = document.querySelector('#register');
	var logout_button = document.querySelector('#logout');
	var account_card = document.querySelector('#account');

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

	document.getElementById('signin').addEventListener('click', function () {
		login_block.style.display = "block";
		registration_block.style.display = "none";
	}, true);

	document.getElementById('register').addEventListener('click', function () {
		login_block.style.display = "none";
		registration_block.style.display = "block";
	}, true);

	// document.querySelector('#login-form').onsubmit = () => {
	// 	const user_email = document.querySelector("#log-email").value;
	// 	const user_password = document.querySelector("#log-password").value

	// 	const login_url = '/auth/login';

	// 	const request = new XMLHttpRequest();

	// 	request.onload = function(){
	// 		try{
	// 			if (request.readyState == XMLHttpRequest.DONE) {
	// 				if (request.status == 200){
	// 					response = JSON.parse(request.responseText);
	// 					if (response.login){
	// 						console.log('already in');
	// 						var flash_message = document.createElement('div');
	// 						flash_message.innerHTML = '<p>You have log in successfully</p>';
	// 						flash_message.className = 'flash_message';
	// 						login_block.style.display = 'none';
	// 						registration_block.style.display = 'none';
	// 						main_container.style.display = 'flex';
	// 						main_container.append(flash_message);
	// 						signin_button.style.display = 'none';
	// 						register_button.style.display = 'none';
	// 						logout_button.style.display = 'block';
	// 						account_card.style.display = 'block';

	// 					}
	// 				}

	// 				else{
	// 					console.log('Something really bad happend');
	// 				}
	// 			}
	// 		}catch(e){
	// 			console.log(e)
	// 		}
	// 	}

	// 	request.open('POST', window.origin + login_url, true);

	// 	const input = new FormData();
	// 	input.append('email', user_email);
	// 	input.append('password', user_password);

	// 	request.send(input);

	// 	return false;
	// }

	// document.querySelector('#logout').onclick = () => {
	// }

	// document.querySelector('#registration-form').onsubmit = () => {
	// 	// const request = new XMLHttpRequest();
	// 	const user_name = document.querySelector("#reg-name").value;
	// 	const user_email = document.querySelector("#reg-email").value;
	// 	const user_password = document.querySelector("#reg-password").value;

	// 	// request.open('POST', `${window.origin}/register`);

	// 	const input = new FormData();
	// 	input.append('name', user_name);
	// 	input.append('email', user_email);
	// 	input.append('password', user_password);

	// 	const registration_url = '/auth/register';

	// 	const request = new XMLHttpRequest();

	// 	request.onload = function(){
	// 		try{
	// 			if (request.readyState == XMLHttpRequest.DONE) {
	// 				if (request.status == 200){
	// 					console.log(JSON.parse(request.responseText));
	// 				}

	// 				else{
	// 					console.log('Something really bad happend');
	// 				}
	// 			}
	// 		}catch(e){
	// 			console.log(e)
	// 		}
	// 	}

	// 	request.open('POST', window.origin + registration_url, true);

	// 	request.send(input);


	// 	return false;
	// }
});


