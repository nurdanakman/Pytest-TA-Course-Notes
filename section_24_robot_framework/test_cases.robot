*** Settings ***
Library  RequestsLibrary


*** Variables ***
${Application_URL}  https://thetestingworldapi.com


*** Test Cases ***
TC_001_Get_Request
    ${url}=  Set Variable  HelloWorld
    Log To Console  ${Application_URL}
    Log To Console  ${url}