// alert('Hello I am here for you sir');
document.addEventListener('DOMContentLoaded', () => {

	var login_block = document.querySelector('#login-block');
	var registration_block = document.querySelector('#registration-block');
	var main_container = document.querySelector('#main-container');
	var main_screen = document.querySelector('#main-screen');
	var register_button = document.querySelector('#register');
	var logout_button = document.querySelector('#logout');
	var account_card = document.querySelector('#account');
	var create_channel_button = document.querySelector('#create_channel_button');
	var join_channel_button = document.querySelector('#join_channel_button');
	var start_conversation_button = document.querySelector('#start_conversation_button');
	var start_channel_button = document.querySelector('#start_channel_button');
	var search_channel_button = document.querySelector('#search_channel_button');
	var search_people_button = document.querySelector('#search_people_button');
	var registration_button = document.querySelector('#registration_button');
	var signin_button = document.querySelector('#signin_button');

	const test_template = Handlebars.compile(document.querySelector('#result').innerHTML);
	const create_channel_template = Handlebars.compile(document.querySelector('#channel-creation').innerHTML);
	const join_channel_template = Handlebars.compile(document.querySelector('#join-channel').innerHTML);
	const join_conversation_template = Handlebars.compile(document.querySelector('#join-conversation').innerHTML);

	window.onpopstate = function(event) {
		main_screen.innerHTML = event.state['data'];
	};

	window.addEventListener('click', async function(event){
		if(event.target == start_conversation_button){
			var response = make_request('GET', '/user/conversation', 'Start Conversation', join_conversation_template());
		}
		if(event.target == create_channel_button){
			make_request('GET', '/user/create-channel', 'Create Channel', create_channel_template());
		}
		if(event.target == join_channel_button){
			make_request('GET', '/user/join-channel', 'Join Channel', join_channel_template());
		}
		if(event.target == start_channel_button){
			make_request('POST', window.location.pathname)
		}
		if(event.target == search_channel_button){
			make_request('POST', window.location.pathname)
		}
		if(event.target == search_people_button){
			make_request('POST', window.location.pathname)
		}
	})

	function make_request(method, url, name, template){
		const request = new XMLHttpRequest();
		let response; 

		request.open(method, url);

		request.onload = function(){
			if (request.readyState == XMLHttpRequest.DONE){
				if(request.status == 200){
					response = request.responseText;
					document.querySelector('#main-screen').innerHTML = template;
					history.pushState({data: `${template}`}, name, url);
					document.title = name;
				}else{
					console.log('Doing bad');
				}
			}
		}

		request.send();

		return response;
		// return false;
	}


//Clean the following code:=========================== 
// TODO: Clean up the code with clear and consise methods


	var valid_password = false;
	var matching_password = false;
	var valid_email = false;
	var valid_name = false;
	var valid_login_email = false;
	var valid_login_password = false;
	var channel_name_value = false;
	var channel_description_value = false;

	document.querySelector('#channel_name').onkeyup =  () => {
		if(document.querySelector('#channel_name').value.lenght > 0) {
			channel_name_value = true;
			start_channel_button.disabled = false;
			// if(channel_description_value && channel_description_value) {
			// 	start_channel_button.disabled = false;
			// }
			// else{
			// 	start_channel_button.disabled = true;
			// }
		}
		else{
			start_channel_button.disabled = true;
		}
	}

	document.querySelector('#channel_description').onkeyup =  () => {
		if(document.querySelector('#channel_description').value.length > 0) {
			channel_description_value = true;
			start_channel_button.disabled = false;
			// if(channel_description_value && channel_description_value) {
			// 	start_channel_button.disabled = false;
			// }
			// else{
			// 	start_channel_button.disabled = true;
			// }
		}
		else{
			start_channel_button.disabled = true;
		}
	}

	document.querySelector('#log-email').onkeyup =  () => {
		const validEmailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
		if(document.querySelector('#log-email').value.match(validEmailFormat)) {
			valid_login_email = true;
			if(valid_login_email && valid_login_password) {
				signin_button.disabled = false;
			}
			else{
				signin_button.disabled = true;
			}
		}
		else{
			signin_button.disabled = true;
		}
	}

	document.querySelector('#log-password').onkeyup =  () => {
		const validPasswordFormat = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,25}$/;
		if(document.querySelector('#log-password').value.match(validPasswordFormat)) {
			valid_login_password = true;
			if(valid_login_email && valid_login_password) {
				signin_button.disabled = false;
			}
			else{
				signin_button.disabled = true;
			}
		}
		else{
			signin_button.disabled = true;
		}
	}

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


