*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections
Resource  Resources/UserKeyword.robot


*** Variables ***
${Base_URL}  https://thetestingworldapi.com/
${Student_ID}   7117374

*** Test Cases ***
TC_001_Fetch_Student_Details_with_Keyword
    [Setup]         Welcome User
    [Teardown]      End TestCase
    Fetch and Validate Get Status Code  50  200
    ${response}=  Fetch and Return Get Response  700500
    log to console  ${response.content}
    ${response1}=  Fetch and Return Get Response  700501
    log to console  ${response1.content}