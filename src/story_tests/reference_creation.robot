*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
When article form is selected article form is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  article
    Page Should Contain  Creating article type reference

When book form is selected book form is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference

When book form is selected book form is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  misc
    Page Should Contain  Creating misc type reference

When Article Is Submitted Page Should Redirect To Main
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  article
    Page Should Contain  Creating article type reference
    Set Name  Referenssi 1
    Set Author  Kirjoittaja
    Set Title  Kirjoitus
    Set Journal  Sanomalehti
    Set Year  1999
    Click Button  submit
    Main Page Should Be Open

When Posting Article Without Author Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  article
    Page Should Contain  Creating article type reference
    Set Name  Referenssi 2
    Set Title  Kirjoitus
    Set Journal  Sanomalehti
    Set Year  1999
    Click Button  submit
    Page Should Contain  Author is required
    

*** Keywords ***
Set Name
    [Arguments]  ${name}
    Input Text  name  ${name}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}