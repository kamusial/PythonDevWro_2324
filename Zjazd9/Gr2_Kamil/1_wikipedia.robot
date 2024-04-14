*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${wikipedia login}    RobotTests
${wikipedia password}    RobotFrameworkA

*** Keywords ***


*** Test Cases ***
First Test
    Open Browser    https://pl.wikipedia.org    chrome
    Maximize Browser Window
    Wait Until Element Is Visible    id:pt-login-2    3    # komentarz
    Click Element    id:pt-login-2
    Sleep    2
    input text    id:wpName1    ${wikipedia login}
    input text    id:wpPassword1    ${wikipedia password}
    select checkbox    id:wpRemember
    click button    id:wpLoginAttempt
    sleep    3
    Wait Until Element Is Visible    id:ca-nstab-project    2
    Capture Page Screenshot
    close browser

