*** Settings ***
Library  RequestsLibrary


*** Variables ***
${Base_URL}  https://thetestingworldapi.com/

*** Test Cases ***
TC_001_Get_Request
    create session  Get_Student_Details  ${Base_URL}
    ${response}=  get request  Get_Student_Details  api/studentsDetails
    Log To Console    ${response.status_code}   #only response status status_code
    Log To Console    ${response.content}   #response body