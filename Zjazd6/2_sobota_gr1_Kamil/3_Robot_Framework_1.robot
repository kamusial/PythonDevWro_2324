*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Keywords ***


*** Test Cases ***
Test 1
    Open Browser    https://pl.wikipedia.org    chrome
    sleep    1
    Click Element    id:pt-login-2
    sleep    1
    Close Browser