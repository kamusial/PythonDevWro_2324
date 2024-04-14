*** Settings ***
Library    SeleniumLibrary
Test Setup    On start
Test Teardown    On finish

*** Variables ***
${wikipedia login}    RobotTests
${wikipedia correct password}    RobotFramework
${wikipedia wrong password}    1234
${error message}    Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.

*** Keywords ***
Log in wikipedia
    [Arguments]    ${login}=1    ${password}=2
    Wait Until Element Is Visible    id:pt-login-2    3    # komentarz
    Click Element    id:pt-login-2
    Sleep    2
    input text    id:wpName1    ${login}
    input password    id:wpPassword1    ${password}
    run keyword and ignore error      select checkbox    id:wpRemember
    click button    id:wpLoginAttempt

Chech if login passed
    Wait Until Element Is Visible    id:ca-nstab-project    2

Check if login failed
    Wait Until Element Is Visible    xpath://*[@id="userloginForm"]/form/div[1]/div    3
#    Wait Until Element Is Visible  css:.mw-message-box-error    3
    ${my error message}    get text    xpath://*[@id="userloginForm"]/form/div[1]/div
    log    ${my error message}
    log to console    Wiadomosc: ${my error message}
    Should Be Equal    ${my error message}    ${error message}

Search in wikipedia
    [Arguments]  ${text}
    input text    name:search     ${text}
    click button     xpath://*[@id="searchform"]/div/button
    sleep    3

On start
    Open Browser    https://pl.wikipedia.org    chrome
    Maximize Browser Window

On finish
    capture page screenshot
    Close browser

*** Test Cases ***
Successful login
    Log in wikipedia    login=${wikipedia login}     password=${wikipedia correct password}
    Chech if login passed

Failed Login
    Log in wikipedia    login=${wikipedia login}     password=${wikipedia wrong password}
    Check if login failed

Search
    Search in wikipedia    Batman
