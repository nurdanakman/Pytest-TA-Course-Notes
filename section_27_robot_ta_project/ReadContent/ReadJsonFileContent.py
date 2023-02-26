import json
from pathlib import Path


def read_request_content():
    file= open(Path(__file__).parent /'Request.json', 'r')
    json_input = file.read()
    payload = json.loads(json_input)
    return payload
