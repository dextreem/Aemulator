# Aemulator - dextreem (c) 2020
#
# This class represents a challenger that can distribute challenges to the clients

import datetime
import json
from datetime import datetime

from client import Client


class Challenger:
    clients = {}
    task = {}
    data = {}

    def __init__(self):
        self.clients = {
            "localhost": Client("test 1", datetime.now()),
            "192.168.1.20": Client("test 2", datetime.now())
        }
        self.task = {1: "tasks"}
        self.data = {1: "data"}

    def get_challenge_task(self):
        return self.task

    def get_challenge_data(self):
        return self.data

    def register_client(self, ip):
        self.clients[ip] = Client(ip, datetime.now())

    def unregister_client(self, ip):
        self.clients.pop(ip, None)


    def ping(self):
        print("TODO: Ping the server")

    def get_clients(self):
        return {k: v.toJson() for k, v in self.clients.items()}
