*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database

*** Test Cases ***
Created Reference Should Show As Human Readable Text
    Create Article Reference
    Go To References List Page
    ${normal}=  Run Keyword And Return Status    Element Should Be Visible   id=view_normal_format
    Run Keyword If    ${normal}    Click Normal Button If Shown   
    Page Should Contain  Article_Kirjoittaja
    Page Should Contain  Kirjoitus
    Page Should Contain  Sanomalehti
    Page Should Contain  1999

Created Reference Should Show As BibTex
    Create Article Reference
    Go To References List Page
    ${bibtex}=  Run Keyword And Return Status    Element Should Be Visible   id=view_bibtex_format
    Run Keyword If    ${bibtex}    Click BibTex Button If Shown   
    Page Should Contain    Referenssi1
    Page Should Contain  Article_Kirjoittaja
    Page Should Contain  Kirjoitus
    Page Should Contain  Sanomalehti
    Page Should Contain  1999


    

*** Keywords ***
Create Article Reference
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  article
    Page Should Contain  Creating article type reference
    Set Article Information
    Scroll Element Into View  article_submit
    Click Article Submit
    Main Page Should Be Open

Click BibTex Button If Shown
    Click Button  view_bibtex_format

Click Normal Button If Shown
    Click Button  view_normal_format

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
    Set Name  Referenssi1
    Set Author  Article_Kirjoittaja
    Set Title  Kirjoitus
    Set Journal  Sanomalehti
    Set Year  1999