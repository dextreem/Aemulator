# Aemulator - dextreem (c) 2020
#
# This class represents a client (= participant) that can assign to a challenger

import datetime
import json


class Client:
    name = ""
    last_seen = datetime.time()

    def __init__(self, name, last_seen):
        self.name = name
        self.last_seen = last_seen

    def toJson(self):
        return {
            "name": self.name,
            "last_seen": str(self.last_seen),
        }
