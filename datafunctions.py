# Papa's Freezeria Deluxe Bot
# datafunctions.py

# Imports
import json

# Constants
data = {}


# Functions

def load_data():
    global data
    with open("data/settings.json", "r") as file:
        data = json.load(file)


def get_data(key):
    global data

    if len(data) == 0:
        load_data()

    return data[key]


def save_data():
    global data
    with open("data/settings.json", "w") as file:
        json.dump(data, file, indent=4)
