*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.2 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${CREATE_URL}  http://${SERVER}/new_reference
${LIST_URL}    http://${SERVER}/references
${BROWSER}    chrome
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Reset Database
    Go To  ${RESET_URL}

Main Page Should Be Open
    Title Should Be  Main

References Page Should Be Open
    Title Should Be  References

New Reference Page Should Be Open
    Title Should Be  Create a reference

Go To New Reference Page
    Go To  ${CREATE_URL}

Go To References List Page
    Go To  ${LIST_URL}