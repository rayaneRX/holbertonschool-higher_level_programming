#!/usr/bin/python3
"""creates an Object from a “JSON file”:"""

import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”:"""

    with open(filename, "r") as f:
        mm2 = f.read()
        return json.loads(mm2)
