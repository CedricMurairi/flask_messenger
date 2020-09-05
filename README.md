# Flask Messenger

This application is similar to Slack in spirit; I just wanted to know how messaging applications work and explore more about Python and Flask. I decided to build a complicated but straightforward app that enables users to authenticate, create channels, connect with other users, send and receive messages to and from other users, and channels.

I still have some ideas and will be implementing them as I move forward. Creating this has been quite a journey of challenges and lessons on large applications' best practices and core functionalities.

There is still room from improvement, and if you find something you may like to contribute to this app, do not hesitate to contact me, open an issue, or pull-request.

# What I learned

From building this app, I learned a lot about asynchronous programming with Javascript and AJAX to fetch data from the server and keep the user joyful.

I learned a lot about the Handlebars template language since I used it to render the data received from my view function into beautiful cards with visitor details.

I learned and improved my understanding of the Flask framework, the python language, and the Postgresql Database System.

# What I used

To build this project, I could use different tools and techniques; here are my choice

* Flask, for the backed
* Postgresql, for datastorage
* Javascript, for the frontend
* Ajax, async request
* Handlebards, templating language
* Flask SQlalchemy
* Jinja2
* Flask-Migrate
* Flask-Script
* For other dependencies check requirements.txt

# How to install

	$ git clone https://github.com/CedricMurairi/flask_messenger.git

	$ cd flask_messenger

	$ pip3 install -r requirements.txt

	$ export FLASK_APP=manager.py

	$ python3 manage.py create_table

	$ python3 manager.py db init

	$ python3 manage.py db migrate

	$ python3 manager.py db upgrade

	$ flask run

# How to contribute

Kindly pull a request for small changes.

For significant changes, open an issue first, discuss what you want to change, and proceed. 

# Connect with me

http://github.com/CedricMurairi | http://twitter.com/CMurairi | https://www.linkedin.com/in/cedric-murairi/ | http://instagram.com/cedricmurairi/
