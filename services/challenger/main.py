import flask
import json
from datetime import datetime

from client import Client

app = flask.Flask(__name__)
app.config["DEBUG"] = True

clients = {
    1: Client("test 1", datetime.now(), {"localhost", "active"}),
    2: Client("test 2", datetime.now(), {"192.169.2.2", "active"})
}

task = {1: "tasks"}

data = {1: "data"}


@app.route('/', methods=['GET'])
def get_ui():
    print("TODO: Show UI")
    return "<h1>Aemulator</h1><p>In the future you will find an web viewer at this point</p>"


@app.route('/challenge/task', methods=['GET'])
def get_challenge_task():
    print("TODO: Get challenge task")
    return task


@app.route('/challenge/get_data', methods=['GET'])
def get_challenge_data():
    print("TODO: Get challenge data")
    return data


@app.route('/clients', methods=['GET'])
def get_clients():
    print("TODO: Get clients")
    return {k: v.toJson() for k, v in clients.items()}


@app.route('/shutdown', methods=['POST'])
def trigger_shutdown():
    print("TODO: Shutting down")


app.run()
