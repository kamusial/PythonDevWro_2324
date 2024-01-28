*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${wikipedia_login}    RobotTests
${wikipedia_correct_password}    RobotFramework
${wikipedia_NOT_correct_password}    12345
${error_message}    Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.

*** Keywords ***
Log in Wikipedia
    [Arguments]    ${login}    ${password}
    Open Browser    https://pl.wikipedia.org    chrome
    Wait Until Page Contains Element    id:pt-login-2    5
#    Page Should Contain Element    id:pt-login-2
    Click Element    id:pt-login-2
    input text    id:wpName1    ${login}
    Input Password    id:wpPassword1    ${password}
    Checkbox Should Not Be Selected    id:wpRemember
    Click button    id:wpLoginAttempt

*** Test Cases ***
#Successful login
#    Log in Wikipedia    ${wikipedia_login}    ${wikipedia_correct_password}
#    Maximize Browser Window
#    input text    name:search    WSB
#    Press Keys    name:search    RETURN
#    sleep    2
#    Close Browser

Failed login
    Log in Wikipedia    ${wikipedia_login}    ${wikipedia_NOT_correct_password}
    sleep    1
    wait until element is visible    xpath:/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[3]/form/div[1]    5
    sleep    1
    ${my_error_message}    Get Text    xpath:/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[3]/form/div[1]
    log to console    pobrano: ${my_error_message}
    log    pobrano: ${my_error_message}
    Should Be Equal As Strings    ${error_message}    ${my_error_message}