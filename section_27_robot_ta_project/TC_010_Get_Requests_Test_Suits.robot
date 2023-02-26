*** Settings ***
Library  RequestsLibrary
Resource  Resources/UserKeyword.robot
Documentation This suite for geting student details
#test timeout  .1s
#Test Setup  Welcome User
#Test Teardown  End TestCase
Suite Setup  Welcome User
Suite Teardown  End TestCase
#Force Tags  Hello
Default Tags  Hello

*** Variables ***
${Base_URL}  https://thetestingworldapi.com/

*** Test Cases ***
TC_001_Get_Request
    [Tags]  Smoke  Sanity
    create session  Get_Student_Details  ${Base_URL}
    ${response}=  get request  Get_Student_Details  api/studentsDetails
    Log To Console    ${response.status_code}   #only response status status_code
    Log To Console    ${response.content}   #response body

TC_002_Get_Request
    [Tags]  Smoke
    create session  Get_Student_Details  ${Base_URL}
    ${response}=  get request  Get_Student_Details  api/studentsDetails
    Log To Console    ${response.status_code}   #only response status status_code
    Log To Console    ${response.content}   #response body

TC_003_Get_Request
    [Tags]  Smoke  Sanity
    create session  Get_Student_Details  ${Base_URL}
    ${response}=  get request  Get_Student_Details  api/studentsDetails
    Log To Console    ${response.status_code}   #only response status status_code
    Log To Console    ${response.content}   #response body