*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database

*** Test Cases ***
When article form is selected article form is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  article
    Page Should Contain  Creating article type reference

When Article Is Submitted Page Should Redirect To Main
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  article
    Page Should Contain  Creating article type reference
    Set Article Information
    Scroll Element Into View  article_submit
    Click Article Submit
    Main Page Should Be Open

When Posting Article Without Author Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  article
    Page Should Contain  Creating article type reference
    Set Article Information
    Clear Element Text  author
    Scroll Element Into View  article_submit
    Click Article Submit
    Page Should Contain  Please fill out this field.

When Posting Article With Year As A String Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  article
    Page Should Contain  Creating article type reference
    Set Article Information
    Clear Element Text  author
    Clear Element  year
    Set Year  kaksi
    Scroll Element Into View  article_submit
    Click Article Submit
    Page Should Contain  Year must be a number
    

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

Click Article Submit
    Click Button  article_submit

Set Article Information
    Set Name  Referenssi 1
    Set Author  Kirjoittaja
    Set Title  Kirjoitus
    Set Journal  Sanomalehti
    Set Year  1999