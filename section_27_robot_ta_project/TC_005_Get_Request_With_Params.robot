*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections


*** Variables ***
${Base_URL}  https://reqres.in

*** Test Cases ***
TC_001_Get_Request_With_Params
    create session  Get_Param  ${Base_URL}
    &{param}=  create dictionary  page=2    #parameters adding
    ${response}=  get request  Get_Param  api/users  params=${param}

    ${actual_status_code}=  convert to string  ${response.status_code}
    Log To Console    ${actual_status_code}
    should be equal  ${actual_status_code}  200

    Log To Console    ${response.content}   #response body
    ${Json_Resp}=  to json  ${response.content}
    @{page_list}=  get value from json  ${Json_Resp}  page
    ${page_number}=  get from list  ${page_list}  0
    ${actual_page_number}=  convert to string  ${page_number}
    should be equal  ${actual_page_number}  2