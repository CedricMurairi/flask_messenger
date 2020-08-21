// 

var login_block = document.querySelector('#login-block');
var registration_block = document.querySelector('#registration-block');
var main_container = document.querySelector('#main-container');
var main_screen = document.querySelector('#main-screen');
var profile_option_card = document.querySelector('#user_profile_option_card');
var register_button = document.querySelector('#register');
var logout_button = document.querySelector('#logout');
var account_card = document.querySelector('#account');
var create_channel_button = document.querySelector('#create_channel_button');
var join_channel_button = document.querySelector('#join_channel_button');
var start_conversation_button = document.querySelector('#start_conversation_button');
var start_channel_button = document.querySelector('#start_channel_button');
var search_channel_button = document.querySelector('#search_channel_button');
var search_people_button = document.querySelector('#search_people_button');
var channel_name_creation = document.querySelector('#channel_name');
var channel_description = document.querySelector('#channel_description');
// var create_channel_form = document.querySelector('#create_channel_form');
var registration_button = document.querySelector('#registration_button');
var signin_button = document.querySelector('#signin_button');
var channel_title = document.querySelector('#channel_title');
var conversation_title = document.querySelector('#conversation_title');
var channel_list = document.querySelector('#channels');
var conversation_list = document.querySelector('#conversations');
var search_people_list = document.querySelector('#search_people_list');
const channel_card_join = Handlebars.compile(document.querySelector('#channel_card_join_template').innerHTML);
const start_conversation_card = Handlebars.compile(document.querySelector('#start_conversation_card_template').innerHTML);
const button_join_channel_card = document.querySelector('#join-channel-via-card-button');
const button_join_conversation_card = document.querySelector('#start-conversation-via-card-button');

	
document.addEventListener('DOMContentLoaded', () => {

	const test_template = Handlebars.compile(document.querySelector('#result').innerHTML);
	
	console.log(test_template({'age': 20, 'name': 'Yves Shouenard', 'city': 'Las Vegas'}));

// compiling tamplates with handlebars to be used in the channel creation, join and conversation start point
	const create_channel_template = Handlebars.compile(document.querySelector('#channel-creation').innerHTML);
	const join_channel_template = Handlebars.compile(document.querySelector('#join-channel').innerHTML);
	const join_conversation_template = Handlebars.compile(document.querySelector('#join-conversation').innerHTML);

	window.onpopstate = function(event) {
		main_screen.innerHTML = event.state['data'];
	};


	window.addEventListener('click', async function(event){
		if(event.target == start_conversation_button){
			var response = make_get_request('/user/conversation/user', 'Start Conversation', join_conversation_template());
		}
		if(event.target == create_channel_button){
			make_get_request('/user/create-channel', 'Create Channel', create_channel_template());
		}
		if(event.target == join_channel_button){
			make_get_request('/user/join-channel/channels', 'Join Channel', join_channel_template());
		}
		if(event.target == account_card){
			profile_option_card.classList.toggle('hide');
		}
		if(event.target != profile_option_card && event.target != account_card){
			profile_option_card.classList.add('hide');
		}
		if(event.target == channel_title){
			channel_list.classList.toggle('hide');
		}
		if(event.target == conversation_title){
			conversation_list.classList.toggle('hide');
		}
	});


//Clean the following code:=========================== 
// TODO: Clean up the code with clear and consise methods


	// var valid_password = false;
	// var matching_password = false;
	// var valid_email = false;
	// var valid_name = false;
	// var valid_login_email = false;
	// var valid_login_password = false;
	// var channel_name_value = false;
	// var channel_description_value = false;

	// document.querySelector('#channel_name').onkeyup =  () => {
	// 	if(document.querySelector('#channel_name').value.lenght > 0) {
	// 		channel_name_value = true;
	// 		start_channel_button.disabled = false;
	// 		// if(channel_description_value && channel_description_value) {
	// 		// 	start_channel_button.disabled = false;
	// 		// }
	// 		// else{
	// 		// 	start_channel_button.disabled = true;
	// 		// }
	// 	}
	// 	else{
	// 		start_channel_button.disabled = true;
	// 	}
	// }

	// document.querySelector('#channel_description').onkeyup =  () => {
	// 	if(document.querySelector('#channel_description').value.length > 0) {
	// 		channel_description_value = true;
	// 		start_channel_button.disabled = false;
	// 		// if(channel_description_value && channel_description_value) {
	// 		// 	start_channel_button.disabled = false;
	// 		// }
	// 		// else{
	// 		// 	start_channel_button.disabled = true;
	// 		// }
	// 	}
	// 	else{
	// 		start_channel_button.disabled = true;
	// 	}
	// }

	// document.querySelector('#log-email').onkeyup =  () => {
	// 	const validEmailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	// 	if(document.querySelector('#log-email').value.match(validEmailFormat)) {
	// 		valid_login_email = true;
	// 		if(valid_login_email && valid_login_password) {
	// 			signin_button.disabled = false;
	// 		}
	// 		else{
	// 			signin_button.disabled = true;
	// 		}
	// 	}
	// 	else{
	// 		signin_button.disabled = true;
	// 	}
	// }

	// document.querySelector('#log-password').onkeyup =  () => {
	// 	const validPasswordFormat = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,25}$/;
	// 	if(document.querySelector('#log-password').value.match(validPasswordFormat)) {
	// 		valid_login_password = true;
	// 		if(valid_login_email && valid_login_password) {
	// 			signin_button.disabled = false;
	// 		}
	// 		else{
	// 			signin_button.disabled = true;
	// 		}
	// 	}
	// 	else{
	// 		signin_button.disabled = true;
	// 	}
	// }

	// document.querySelector('#reg-email').onkeyup = () => {
	// 	console.log("key Up");
	// 	const validEmailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	// 	if (document.querySelector('#reg-email').value.match(validEmailFormat)) {
	// 		document.querySelector('#correct-email-error').style.color = "green";
	// 		valid_email = true;
	// 		if(valid_email && valid_password && matching_password){
	// 			registration_button.disabled = false;
	// 		}
	// 		else{
	// 			registration_button.disabled = true;
	// 		}
	// 	}
	// 	else {
	// 		document.querySelector('#correct-email-error').style.color = "red";
	// 		valid_email = false;
	// 		registration_button.disabled = true;

	// 	}
	// }

	// document.querySelector('#reg-password').onkeyup = () => {
	// 	const validPasswordFormat = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,25}$/;
	// 	if (document.querySelector('#reg-password').value.match(validPasswordFormat)) {
	// 		document.querySelector('#correct-password-error').style.color = "green";
	// 		valid_password = true;
	// 		if(valid_email && valid_password && matching_password){
	// 			registration_button.disabled = false;
	// 		}
	// 		else{
	// 			registration_button.disabled = true;
	// 		}
	// 	}
	// 	else {
	// 		document.querySelector('#correct-password-error').style.color = "red";
	// 		valid_password = false;
	// 		registration_button.disabled = true;
	// 	}
	// }

	// document.querySelector('#reg-password-repeat').onkeyup = () => {
	// 	if (document.querySelector("#reg-password").value == document.querySelector('#reg-password-repeat').value) {
	// 		document.querySelector('#password-match-error').style.color = "green";
	// 		matching_password = true;
	// 		if(valid_email && valid_password && matching_password){
	// 			registration_button.disabled = false;
	// 		}
	// 		else{
	// 			registration_button.disabled = true;
	// 		}
	// 	}
	// 	else {
	// 		document.querySelector('#password-match-error').style.color = "red";
	// 		matching_password = false;
	// 		registration_button.disabled = true;
	// 	}
	// }

});

function submit_form(element){
	// accessing the form data *data-form* to check the type of form being submitted
	let formData = element.dataset.form;

// make request to create channel
	if(formData == 'create_channel'){

		// getting the respective values submitted with the channel-creation form
		let channelCreationName = element[0].value;
		let channelDescription = element[1].value;
		let keyTerm = ['channel_name', 'channel_description'];
		let data = [channelCreationName, channelDescription];

		let result = make_post_request('/user/create-channel', keyTerm, data);
		console.log(result);
	}

// make request to search for people on the platform
	if(formData == 'search_people'){

		let search_people_name = element[0].value;
		let keyTerm = ['search_people'];
		let data = [search_people_name];

		make_post_request('/user/conversation/user', keyTerm, data, start_conversation_card);
	}

// make request to search for existing channels to join
	if(formData == 'search_channel'){

		let search_channel = element[0].value;
		let keyTerm = ['search_channel'];
		let data = [search_channel];

		make_post_request('/user/join-channel/channels', keyTerm, data, channel_card_join);
	}

	return false;
}


function join_channel_via_button_click(element){
	let id = element.dataset.channel;

	let keyTerm = ['channel_id'];
	let data = [id];

	make_post_request('/user/join-channel/channels/join', keyTerm, data);
}

function join_conversation_via_button_click(element){
	let id = element.dataset.user;
	console.log(id);

	let keyTerm = ['user_id'];
	let data = [id];

	make_post_request('/user/conversation/user/join', keyTerm, data);
}


function make_post_request(url, keyTerm, dataValue, template=null){
	const request = new XMLHttpRequest();
	let response; 

	console.log('Opening request');
	request.open('POST', url);

	console.log('Request onload');
	request.onload = function(){
		if (request.readyState == XMLHttpRequest.DONE){
			if(request.status == 200){
				response = request.responseText;
				console.log(JSON.parse(response));
				var data = JSON.parse(response);
				console.log(data['data']);
				(url == '/user/join-channel/channels') ? document.querySelector('#main-screen').innerHTML += template({'channel_id': data['data']['id'], 'channel_name': data['data']['name'], 'channel_description': data['data']['description'], 'channel_creation': data['data']['created']}) : (url == '/user/conversation/user') ? document.querySelector('#main-screen').innerHTML += template({user: data['response']}) : console.log('get you');
				return response
				// document.querySelector('#main-screen').innerHTML = template;
			}else{
				console.log('Doing bad');
			}
		}
	}

	console.log('Sending request');


	const data = new FormData();

// loop over the parameters passed to the function and append them to the data object to send with the request
	for (var i = 0; i < keyTerm.length; i++) {
		for (var j = i; j < dataValue.length; j++) {
			data.append(keyTerm[i], dataValue[i]);
			break;
		}
	}

	request.send(data);

	console.log('After request');
}


function make_get_request(url, name, template){
	const request = new XMLHttpRequest();
	let response; 

	console.log('Opening request');
	request.open('GET', url);

	console.log('Request onload');
	request.onload = function(){
		if (request.readyState == XMLHttpRequest.DONE){
			if(request.status == 200){
				response = request.responseText;
				console.log('Request passed');
				document.querySelector('#main-screen').innerHTML = template;
				history.pushState({data: `${template}`}, name, url);
				document.title = name;
			}else{
				console.log('Doing bad');
			}
		}
	}

	console.log('Sending request');
	request.send();

	// return response;
	console.log('After request');
}


