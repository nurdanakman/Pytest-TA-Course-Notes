from pathlib import Path
import requests
import json

def test_add_multiple_students():
    url = "https://thetestingworldapi.com/api/studentsDetails"

    f = open(Path(__file__).parent / "new_student_data.json", "r")
    json_input = f.read()
    payload = json.loads(json_input)

    response = requests.post(url, payload)
    print(response.status_code)
    assert response.status_code == 201


