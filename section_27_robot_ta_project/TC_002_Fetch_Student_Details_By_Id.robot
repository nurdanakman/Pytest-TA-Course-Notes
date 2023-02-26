*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections


*** Variables ***
${Base_URL}  https://thetestingworldapi.com/
${Student_ID}   7117374

*** Test Cases ***
TC_001_Fetch_Student_Details_By_Id
    create session  Fetch_Data  ${Base_URL}
    ${response}=  get request  Fetch_Data  api/studentsDetails/${Student_ID}

    ${actual_code}=  convert to string  ${response.status_code}     #convert to the string
    Log To Console     ${response.status_code}
    should be equal  ${actual_code}  200

    Log To Console     ${response.content}
    ${Json_Resp}=  to json  ${response.content}

    @{first_name_list}=  get value from json     ${Json_Resp}  data.first_name
    ${actual_first_name}=  get from list   ${first_name_list}  0
    log to Console  ${actual_first_name}
    should be equal  ${actual_first_name}  Leela

    @{last_name_list}=  get value from json     ${Json_Resp}  data.last_name
    ${actual_last_name}=  get from list   ${last_name_list}  0
    log to Console  ${actual_last_name}
    should be equal  ${actual_last_name}  Balu