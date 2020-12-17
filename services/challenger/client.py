# Aemulator - dextreem (c) 2020
#
# This class represents a client (= participant) that can assign to a challenger

import datetime
import json


class Client:
    name = ""
    last_seen = datetime.time()
    connection = {}

    def __init__(self, name, last_seen, connection):
        self.name = name
        self.last_seen = last_seen
        self.connection = connection

    def toJson(self):
        return {
            "name": self.name,
            "last_seen": str(self.last_seen),
            "connection": str(self.connection)
        }
