// alert('Hello I am here for you sir');
document.addEventListener('DOMContentLoaded', () => {

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
	var search_people_button = document.querySelector('#search_people_button');
	var create_channel_button = document.querySelector('#create_channel_button');
	var registration_button = document.querySelector('#registration_button');
	var signin_button = document.querySelector('#signin_button');

	// window.onload = function(e) {
	// 	e.preventdefault;
	// 	console.log('great job');
	//     make_request('GET', window.location.pathname);
	// }

	window.onpopstate = function(event) {
		if(window.location.pathname == '/'){
			return false;
			// main_screen.innerHTML = "There we go, welcome to the screen";
		}else{
			main_screen.innerHTML = event.state['data'];
		}
	};

	window.onloadstart = function(){console.log('yes onloadstart');}
	window.onloadeddata = function(){console.log('yes onloadeddata');}
	window.onloadedmetadata = function(){console.log('yes onloadedmetadata');}
	window.onload = function(){
		console.log('Yes it\'s loading...');
		// make_request('GET', '/user/conversation', 'Home');
		console.log('You won\'t see me coming');
		if(window.location.pathname == '/user/conversation'){
			make_request('GET', '/', 'Home', false);
		}
	}

	window.addEventListener('click', function(event){
		if(event.target == start_conversation_button){
			var response = make_request('GET', '/user/conversation', 'Start Conversation');
			console.log(response);
		}
		if(event.target == create_channel_button){
			var response = make_request('GET', '/user/create-channel', 'Create Channel');
		}
		if(event.target == join_channel_button){
			var response = make_request('GET', '/user/join-channel', 'Join Channel');
		}
	})

	function make_request(method, url, name, async=true){
		const request = new XMLHttpRequest();
		let response; 

		request.open(method, url, async);

		request.onload = function(){
			if (request.readyState == XMLHttpRequest.DONE){
				if(request.status == 200){
					response = request.responseText;
					main_screen.innerHTML = `<div>${response}</div>`;
					history.pushState({data: `${response}`}, name, url);
				}else{
					console.log('Doing bad');
				}
			}
		}

		request.send();

		return response;
		// return false;
	}

	var valid_password = false;
	var matching_password = false;
	var valid_email = false;
	var valid_name = false;

	document.querySelector('#reg-email').onkeyup = () => {
		console.log("key Up");
		const validEmailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
		if (document.querySelector('#reg-email').value.match(validEmailFormat)) {
			document.querySelector('#correct-email-error').style.color = "green";
			valid_email = true;
			if(valid_email && valid_password && matching_password){
				registration_button.disabled = false;
			}
			else{
				registration_button.disabled = true;
			}
		}
		else {
			document.querySelector('#correct-email-error').style.color = "red";
			valid_email = false;
			registration_button.disabled = true;

		}
	}

	document.querySelector('#reg-password').onkeyup = () => {
		const validPasswordFormat = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,25}$/;
		if (document.querySelector('#reg-password').value.match(validPasswordFormat)) {
			document.querySelector('#correct-password-error').style.color = "green";
			valid_password = true;
			if(valid_email && valid_password && matching_password){
				registration_button.disabled = false;
			}
			else{
				registration_button.disabled = true;
			}
		}
		else {
			document.querySelector('#correct-password-error').style.color = "red";
			valid_password = false;
			registration_button.disabled = true;
		}
	}

	document.querySelector('#reg-password-repeat').onkeyup = () => {
		if (document.querySelector("#reg-password").value == document.querySelector('#reg-password-repeat').value) {
			document.querySelector('#password-match-error').style.color = "green";
			matching_password = true;
			if(valid_email && valid_password && matching_password){
				registration_button.disabled = false;
			}
			else{
				registration_button.disabled = true;
			}
		}
		else {
			document.querySelector('#password-match-error').style.color = "red";
			matching_password = false;
			registration_button.disabled = true;
		}
	}

});


