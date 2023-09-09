import json


def load_notes():
    try:
        with open('notes.json', 'r') as f:
            notes = json.load(f)

    except FileNotFoundError:
        notes = {}

    return notes


