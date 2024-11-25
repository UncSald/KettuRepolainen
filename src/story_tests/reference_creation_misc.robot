*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database

*** Test Cases ***
When misc form is selected misc form is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  misc
    Page Should Contain  Creating misc type reference

When Misc Is Submitted Page Should Redirect To Main
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  misc
    Page Should Contain  Creating misc type reference
    Set Misc Information
    Click Misc Submit
    Main Page Should Be Open

*** Keywords ***
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
    Set Author  Kirjoittaja
    Set Title  Kirjoitus
    Set Howpublished  Sanomalehti
    Set Year  1999