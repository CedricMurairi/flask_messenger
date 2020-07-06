import os

from flask import Flask, render_template, request, jsonify, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_folder='statics')
app.config["SECRET_KEY"] = "kajdoijwoI#)(@#)(@#&(!)#*(*!@##UHJEWDGYUEUGFjheo8w3492uiou(*u897rg8923900"
engine = create_engine('postgresql:///cedricmurairi')
db = scoped_session(sessionmaker(bind=engine))
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/register_user", methods=["POST"])
def register():
    request_data = request.get_json()
    name = request_data.get('name')
    email = request_data.get('email')
    password = request_data.get('password')

    print(request_data)

    check_user_exist = db.execute('SELECT * FROM flaskUsers WHERE name = :name AND email = :email',
                                  {"name": name, "email": email}).fetchone()

    if(check_user_exist):
        return jsonify({"registered": False, "error": "User already exist with the same name and email"})

    db.execute('INSERT INTO flaskUsers (name, email, password) VALUES (:name, :email, :password)',
    			{"name": name, "email": email, "password": password})
    db.commit()
    return jsonify({"registered": True})


@app.route("/login_user", methods=["POST"])
def login():
    request_data = request.get_json()
    email = request_data.get('email')
    password = request_data.get('password')

    result = db.execute('SELECT * FROM flaskUsers WHERE email = :email AND password = :password',
                        {"email": email, "password": password}).fetchone()

    if result:
        session['name'] = result.name
        session['email'] = result.email
        return jsonify({"login": True, "result": [row for row in result]})
    return jsonify({"login": False, "error": "User entered a wrong email or password"})


@app.route('/logout', methods=["POST"])
def logout():
    session.pop('name')
    session.pop('email')
    return jsonify({"logout": True})


socketio.on('send message')


def send_message(data):
    message = data['message']
    emit('recieve message', {'message': message}, broadcast=True)

if __name__ == '__main__':
    app.run(debug=True)