*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
References Site Is Open
    Go To  ${HOME_URL}
    Click Link  references
    Title Should Be  References


*** Keywords ***
Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  author  ${title}

References Page Should Be Open
    Title Should Be  References
