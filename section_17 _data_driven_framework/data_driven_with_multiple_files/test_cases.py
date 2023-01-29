from pathlib import Path
import requests
import json
import openpyxl
from data_driven_with_multiple_files import library

def test_add_multiple_students():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open(Path(__file__).parent.parent / "new_student_data.json", "r")
    json_input = f.read()
    payload = json.loads(json_input)


    obj = library.Common(Path(__file__).parent.parent / "new_student_data.xlsx", "Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range(2, row+1):
        updated_payload = obj.update_request_with_data(i,payload, keyList)

        response = requests.post(url, updated_payload)
        print(response.status_code)