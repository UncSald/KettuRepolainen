*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database

*** Test Cases ***



Created Reference Should Show As Human Readable Text
    Create Misc Reference
    Go To References List Page
    Page Should Contain  Misc_Kirjoittaja
    Page Should Contain  Kirjoitus
    Page Should Contain  Sanomalehti
    Page Should Contain  1999

Created Reference Should Show As BibTex
    Create Misc Reference
    Go To References List Page
    Click Button  view_bibtex_format
    Page Should Contain    Referenssi 1
    Page Should Contain  Misc_Kirjoittaja
    Page Should Contain  Kirjoitus
    Page Should Contain  Sanomalehti
    Page Should Contain  1999


*** Keywords ***
Create Misc Reference
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  misc
    Page Should Contain  Creating misc type reference
    Set Misc Information
    Scroll Element Into View  misc_submit
    Click Misc Submit
    Main Page Should Be Open

Set Name
    [Arguments]  ${name}
    Input Text  xpath=//form[@id='misc']//input[@name='name']  ${name}

Set Author
    [Arguments]  ${author}
    Input Text  xpath=//form[@id='misc']//input[@name='author']  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  xpath=//form[@id='misc']//input[@name='title']  ${title}

Set Howpublished
    [Arguments]  ${howpublished}
    Input Text  xpath=//form[@id='misc']//input[@name='howpublished']  ${howpublished}

Set Year
    [Arguments]  ${year}
    Input Text  xpath=//form[@id='misc']//input[@name='year']  ${year}

Click Misc Submit
    Click Button  misc_submit

Set Misc Information
    Set Name  Referenssi 1
    Set Author  Misc_Kirjoittaja
    Set Title  Kirjoitus
    Set Howpublished  Sanomalehti
    Set Year  1999