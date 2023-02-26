*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections


*** Variables ***
${Base_URL}  https://thetestingworldapi.com/
${Student_ID}  7117001

*** Test Cases ***
TC_001_Delete_Student
    create session  Delete_Data  ${Base_URL}
    ${response}=  delete request  Delete_Data  api/studentsDetails/${Student_ID}

    ${actual_status_code}=  convert to string  ${response.status_code}
    Log To Console    ${actual_status_code}
    should be equal  ${actual_status_code}  200

    Log To Console    ${response.content}
    ${Json_Resp}=  to json  ${response.content}
    @{status_list}=  get value from json  ${Json_Resp}  status
    ${actual_status}=  get from list  ${status_list}  0
    should be equal  ${actual_status}  true