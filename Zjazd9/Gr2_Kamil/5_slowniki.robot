*** Settings ***
Library    Collections

*** Test Cases ***
Slowniki
    ${czlowiek}    create dictionary    name=Kamil    Age=18    hobby=brak
    ${imie}    get from dictionary    ${czlowiek}    name
    log to console   ${imie}

    ${auto}    set variable    Audi
    set to dictionary    ${czlowiek}    color=red    auto=${auto}
    log to console   ${czlowiek}

    ${usuniete}    pop from dictionary    ${czlowiek}    hobby
    log to console    usunieto element o kluczu hobby, wartosc: ${usuniete}

    remove from dictionary    ${czlowiek}    color
    log to console    ${czlowiek}