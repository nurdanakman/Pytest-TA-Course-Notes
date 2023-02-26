
*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections
Resource  Resources/UserKeyword.robot


*** Variables ***
${Base_URL}  https://thetestingworldapi.com/

*** Test Cases ***
TC_001_Post_Student_Details
    [Tags]  Smoke Regression
    create session  Add_Data  ${Base_URL}
    ${payload}=  Fetch Request Content
    &{header}=  create dictionary  Content-Type=application/json
    ${response}=  post request  Add_Data  api/studentsDetails  data=${payload}  headers=${header}
    log to console  ${response.status_code}
    log to console  ${response.content}