*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Keywords ***


*** Test Cases ***
First Test
    open browser    https://pl.wikipedia.org    chrome
    click element    id:pt-login-2
    sleep    2
    input text    id:wpName1    Kamil
    input text    id:wpPassword1    Haslo
    select checkbox    id:wpRemember
    click button    id:wpLoginAttempt
    sleep    3
    close browser

