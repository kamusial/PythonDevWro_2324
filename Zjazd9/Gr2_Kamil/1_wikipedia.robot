*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${wikipedia login}    RobotTests
${wikipedia correct password}    RobotFramework
${wikipedia wrong password}    1234
${error message}    Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.

*** Keywords ***
Log in wikipedia
    [Arguments]    ${login}=1    ${password}=2
    Open Browser    https://pl.wikipedia.org    chrome
    Maximize Browser Window
    Wait Until Element Is Visible    id:pt-login-2    3    # komentarz
    Click Element    id:pt-login-2
    Sleep    2
    input text    id:wpName1    ${login}
    input password    id:wpPassword1    ${password}
    select checkbox    id:wpRemember
    click button    id:wpLoginAttempt

*** Test Cases ***
Successful login
    Log in wikipedia    login=${wikipedia login}     password=${wikipedia correct password}
    Wait Until Element Is Visible    id:a-nstab-project    2
    Capture Page Screenshot
    close browser

Failed Login
    Log in wikipedia    login=${wikipedia login}     password=${wikipedia wrong password}
    Wait Until Element Is Visible    xpath://*[@id="userloginForm"]/form/div[1]/div    3
#    Wait Until Element Is Visible  css:.mw-message-box-error    3
    ${my error message}    get text    xpath://*[@id="userloginForm"]/form/div[1]/div
    log    ${my error message}
    log to console    Wiadomosc: ${my error message}