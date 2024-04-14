*** Settings ***
Library    Collections

*** Variables ***
@{my_list}  1  2  3  4
${zmienna}  4

*** Test Cases ***
Listy
    append to list    ${my_list}    4
    append to list    ${my_list}    wyraz
    log to console    ${my_list}

    @{my_list}  Remove Duplicates  ${my_list}
    log to console    ${my_list}

    Remove From List  ${my_list}     0
    log to console     ${my_list}

    Remove Values From List  ${my_list}  2  3
    log to console   ${my_list}

    append to list  ${my_list}  5
    log list  ${my_list}

    List Should Contain Value  ${my_list}  5