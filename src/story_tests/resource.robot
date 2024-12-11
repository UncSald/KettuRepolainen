*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.2 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${CREATE_URL}  http://${SERVER}/new_reference
${LIST_URL}    http://${SERVER}/references
${BROWSER}    Chrome
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Run Keyword If    '${HEADLESS}' == 'true'    Call Method    ${options}    add_argument    --headless
    Open Browser    ${HOME_URL}    ${BROWSER}    options=${options}
    Set Selenium Speed    ${DELAY}

Reset Database
    Go To    ${RESET_URL}


Main Page Should Be Open
    Title Should Be  Create a reference

References Page Should Be Open
    Title Should Be  References

New Reference Page Should Be Open
    Title Should Be  Create a reference

Go To New Reference Page
    Go To  ${CREATE_URL}

Go To References List Page
    Go To  ${LIST_URL}