document.addEventListener('DOMContentLoaded', function() {
	
	let name_input = document.querySelector('#name_input');
	let display_msg = document.querySelector('#welcome_msg');

	name_input.addEventListener('keyup', function(event) {
		let display_msg = document.querySelector('#welcome_msg');
		if (name_input.value) {
			display_msg.innerHTML = `Welcome, ${name_input.value}! This is Raghav\'s Home Page!`;
		}
		else {
			display_msg.innerHTML = 'Welcome! This Raghav\'s Home Page!';
		}
	});
});
