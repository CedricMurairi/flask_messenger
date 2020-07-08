// alert('Hello I am here for you sir');
document.addEventListener('DOMContentLoaded', () => {

	// window.onpopstate() = function(){
	// 	console.log('state poped');
	// }

	var login_block = document.querySelector('#login-block');
	var registration_block = document.querySelector('#registration-block');
	var main_container = document.querySelector('#main-container');
	var main_screen = document.querySelector('#main-screen');
	var signin_button = document.querySelector('#signin');
	var register_button = document.querySelector('#register');
	var logout_button = document.querySelector('#logout');
	var account_card = document.querySelector('#account');
	var create_chanel_block = document.querySelector('#create-channel');
	var join_conversation_block = document.querySelector('#join_conversation');
	var join_conversation_block = document.querySelector('#join_conversation');
	var create_channel_button = document.querySelector('#create_channel_button');
	var join_channel_button = document.querySelector('#join_channe_button');
	var start_conversation_button = document.querySelector('#start_conversation_button');
	var handle_template = document.querySelector('#content').innerHTML;

	start_conversation_button.addEventListener('click', function(){
		var response = make_request('GET', '/user/conversation', 'Start Conversation');
	});

	create_channel_button.addEventListener('click', function(){
		var response = make_request('GET', '/user/create-channel', 'Create Channel');

	});

	join_channel_button.addEventListener('click', function(){
		var response = make_request('GET', '/user/join-channel', 'Join Channel');
	});


	function make_request(method, url, name){
		const request = new XMLHttpRequest();

		request.open(method, url);

		request.onload = function(){
			if (request.readyState == XMLHttpRequest.DONE){
				if(request.status == 200){
					const response = request.responseText;
					main_screen.innerHTML = `<div>${response}</div>`;
					history.pushState(response, name, url)
				}else{
					console.log('Doing bad');
				}
			}
		}

		request.send()

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

	document.getElementById('signin').addEventListener('click', function () {
		login_block.style.display = "block";
		registration_block.style.display = "none";
	}, true);

	document.getElementById('register').addEventListener('click', function () {
		login_block.style.display = "none";
		registration_block.style.display = "block";
	}, true);

});


