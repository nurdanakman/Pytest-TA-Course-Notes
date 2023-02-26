*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections
Library  ../ReadContent/ReadJsonFileContent.py


*** Variables ***
${Base_URL}  https://thetestingworldapi.com/


*** Keywords ***
Fetch and Validate Get Status Code
    [Arguments]  ${student_id}  ${expectedStatusCode}
    [Setup]         Welcome User
    [Teardown]      End TestCase
    #[Documentation] This keyword for some fetching and validating data
    #[Timeout]  .100s
    create session  SName  ${Base_URL}
    ${response}=  get request  SName  api/studentsDetails/${student_id}
    ${statusC}=  convert to string  ${response.status_code}
    should be equal  ${expectedStatusCode}   ${statusC}

Fetch and Return Get Response
    [Arguments]  ${student_id}
    create session  SName  ${Base_URL}
    ${response}=  get request  SName  api/studentsDetails/${student_id}
    [Return]  ${response}

Fetch Request Content
    ${jsonBody}=  read_request_content
    [Return]  ${jsonBody}

Welcome User
    [Documentation]  Welcome the start test Cases
    log to console  new test case start

End TestCase
    [Documentation]  Test Case completed
    log to console  test case is completed
