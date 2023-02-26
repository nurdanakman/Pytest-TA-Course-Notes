*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections


*** Variables ***
${Base_URL}  https://thetestingworldapi.com/
${origin_first_name}  Nurdan
${updated_first_name}  Nurdan1
${Student_ID}  7117001


*** Test Cases ***
TC_007_End_to_End_TestCase
    [Timeout]  .2s
    [Documentation]  This test case is related to end to end test execution
    create session  E2E  ${Base_URL}
    &{payload}=  create dictionary  first_name=${origin_first_name}  middle_name=X  last_name=Akman  date_of_birth=14/04/1996
    &{header}=  create dictionary  Content-Type=application/json
    ${post_response}=  post request  E2E  api/studentsDetails  data=${payload}  headers=${header}
    log to Console  ${post_response.content}

    ${json_resp}=  to json  ${post_response.content}
    ${id_list}=  get value from json  ${json_resp}  id
    ${id}=  get from list  ${id_list}  0
    log to console  ${id}

    &{payload_updated}=  create dictionary  id=${id}  first_name=${updated_first_name}  middle_name=X  last_name=Akman  date_of_birth=14/04/1996
    ${put_response}=  put request  E2E  api/studentsDetails/${id}  data=${payload_updated}  headers=${header}
    log to console  ${put_response.content}
    log to console  ${put_response.status_code}


   # ${get_response}=  get request  E2E  api/studentsDetails/${id}
   # ${json_resp}=  to json  ${get_response.content}
   # ${first_name_list}=  get value from json  ${json_resp}  data.first_name
   # ${first_name}=  get from list  ${first_name_list}  0
   # should be equal  ${first_name}  ${updated_first_name}

    Fetch Details and Validate  ${id}

    ${delete_response}=  delete request  E2E  api/studentsDetails/${id}
    Log To Console    ${delete_response.status_code}
    ${delete_json}=  to json  ${delete_response.content}
    ${delete_status_list}=  get value from json  ${delete_json}  status
    ${status}=  get from list  ${delete_status_list}  0
    should be equal  ${status}  true


*** Keywords ***
Fetch Details and Validate
    [Arguments]  ${id}
    ${get_response}=  get request  E2E  api/studentsDetails/${id}
    ${json_resp}=  to json  ${get_response.content}
    ${first_name_list}=  get value from json  ${json_resp}  data.first_name
    ${first_name}=  get from list  ${first_name_list}  0
    should be equal  ${first_name}  ${updated_first_name}