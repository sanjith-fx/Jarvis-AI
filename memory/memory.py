import json

FILE = "data/memory.json"


def save_memory(data):

    with open(FILE, "w") as f:

        json.dump(data, f, indent=4)


def load_memory():

    try:

        with open(FILE, "r") as f:

            return json.load(f)

    except:

        return {}