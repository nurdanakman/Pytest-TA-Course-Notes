
*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections


*** Variables ***
${Base_URL}  https://thetestingworldapi.com/

*** Test Cases ***
TC_001_Post_Student_Details
    create session  Add_Data  ${Base_URL}
    &{payload}=  create dictionary  first_name=Nurdan  middle_name=X  last_name=Akman  date_of_birth=14/04/1996
    &{header}=  create dictionary  Content-Type=application/json
    ${response}=  post request  Add_Data  api/studentsDetails  data=${payload}  headers=${header}


    ${actual_code}=  convert to string  ${response.status_code}     #convert to the string
    Log To Console     ${response.status_code}
    should be equal  ${actual_code}  201

    Log To Console     ${response.content}
    ${Json_Resp}=  to json  ${response.content}

    @{first_name_list}=  get value from json     ${Json_Resp}  first_name
    ${actual_first_name}=  get from list   ${first_name_list}  0
    log to Console  ${actual_first_name}
    should be equal  ${actual_first_name}  Nurdan