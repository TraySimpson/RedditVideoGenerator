import json
import os


def add_to_json(video_id):
    filename = 'database.json'

    with open(filename, 'r') as f:
        data = json.load(f)
    data.append({"video_id": video_id})

    with open(filename, 'w') as f:
        json.dump(data, f)


def get_list():
    filename = 'database.json'

    with open(filename, 'r') as f:
        data = json.load(f)
    return data
