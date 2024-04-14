*** Variables ***
${string}    piesek
@{list}    pierwszy    drugi    trzeci    czwarty    piaty
@{list_of_numbers}    1    2    3    4    5
@{imiona}    Kamil    Kamila    Jakub    Matria    Augusto
&{dictionary}    slowo=${string}    numer=30    lista=@{list}
@{to print}    Test do wyswietlenia    STDOUT    TRUE    >5

*** Test Cases ***
For loop in range 10
    FOR    ${i}   IN RANGE    10
        log to console    Liczba to: ${i}
    END

For loop in range 3 30 4
    FOR    ${i}   IN RANGE    3    30    7
        log to console    Liczba to: ${i}
    END

For Loop in Dictionary
    log to console    ${dictionary}
    FOR    ${keys_and_values}    IN    &{dictionary}
        log to console    ${keys_and_values}
    END

For Loop in List
    log to console    ${imiona}
    FOR    ${imie}    IN    @{imiona}
        IF    '${imie}' == 'Kamila'    log to console    Imie to: ${imie}
    END

For Loop in List
    FOR    ${number}    IN    @{list_of_numbers}
        IF    ${number} == 3    log    Numer to: ${number}
    END