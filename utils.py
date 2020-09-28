import json

def read_json(path):
    with open('./resource/' + path, encoding='utf8') as f:
        return json.load(f)

def write_json(path, data):
    with open('./resource/' + path, encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=True, indent=4)