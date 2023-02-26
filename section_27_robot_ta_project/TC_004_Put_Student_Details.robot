
*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections


*** Variables ***
${Base_URL}  https://thetestingworldapi.com/
${Student_ID}   7117512

*** Test Cases ***
TC_001_Put_Student_Details
    create session  Update_Data  ${Base_URL}
    &{payload}=  create dictionary  id=${Student_ID}    first_name=Nurdan  middle_name=Y  last_name=Akman  date_of_birth=14/04/1996
    &{header}=  create dictionary  Content-Type=application/json
    ${response}=  put request  Update_Data  api/studentsDetails/${Student_ID}  data=${payload}  headers=${header}


    ${actual_code}=  convert to string  ${response.status_code}     #convert to the string
    Log To Console     ${response.status_code}
    should be equal  ${actual_code}  200

    Log To Console     ${response.content}
    ${Json_Resp}=  to json  ${response.content}

    @{status_list}=  get value from json     ${Json_Resp}  status
    ${actual_status}=  get from list   ${status_list}  0
    log to Console  ${actual_status}
    should be equal  ${actual_status}  true