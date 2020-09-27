import json

def import_json(path):
    with open(path, 'r') as f:
        return json.load(f)