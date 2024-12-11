*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database

*** Test Cases ***
References Site Is Open
    Go To  ${HOME_URL}
    Click Link  references
    Title Should Be  References

New Reference Site Is Open
    Go To  ${HOME_URL}
    Click Link  new_reference
    Title Should Be  Create a reference


*** Keywords ***
Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  author  ${title}

References Page Should Be Open
    Title Should Be  References
