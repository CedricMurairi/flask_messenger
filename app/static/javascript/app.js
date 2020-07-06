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

});


