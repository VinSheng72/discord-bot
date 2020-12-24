import json
import random

def read_json(path):
    with open('./resource/' + path, mode='r', encoding='utf8') as f:
        return json.load(f)

def write_json(path, data):
    with open('./resource/' + path, mode='w', encoding='utf8') as f:
        f.seek(0)
        json.dump(data, f, ensure_ascii=True, indent=4)
        f.truncate()

def write_txt(path, data):
    with open('./resource/' + path, 'a+', encoding="utf-8") as f:
        f.write(data + '\n')

def any(list1, list2):
    for x in list1:
        if(x in list2):
            return True
    return False