import flask
import json
from datetime import datetime
from flask import request

from client import Client
from challenger import Challenger

app = flask.Flask(__name__)
app.config["DEBUG"] = True

challenger = Challenger()


@app.route('/', methods=['GET'])
def get_ui():
    print("TODO: Show UI")
    return "<h1>Aemulator</h1><p>In the future you will find an web viewer at this point</p>"


@app.route('/shutdown', methods=['POST'])
def trigger_shutdown():
    print("TODO: Shutting down")


@app.route('/challenge/task', methods=['GET'])
def get_challenge_task():
    return challenger.get_challenge_data()


@app.route('/challenge/get_data', methods=['GET'])
def get_challenge_data():
    return challenger.get_challenge_data()


@app.route('/clients/register', methods=['POST'])
def register_client():
    challenger.register_client(request.remote_addr)
    return "true"


@app.route('/clients/unregister', methods=['POST'])
def unregister_client():
    challenger.unregister_client(request.remote_addr)
    return "true"


@app.route('/clients/ping', methods=['POST'])
def ping():
    challenger.ping()


@app.route('/clients/all', methods=['GET'])
def get_clients():
    return challenger.get_clients()


app.run()
