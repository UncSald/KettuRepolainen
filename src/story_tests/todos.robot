*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
After adding a reference, there is one reference
    Go To  ${HOME_URL}
    Click Link  new_reference
    References Should Be Open
    Set Author  Aleksis Kivi
    Set Title  Seitsemän Veljestä
    Click Button  submit
    Go To  ${HOME_URL}
    Click Link  reference_list
    Page Should Contain  Aleksis Kivi

*** Keywords ***
Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  author  ${title}