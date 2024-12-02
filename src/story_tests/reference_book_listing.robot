*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database


*** Test Cases ***
Created Reference Should Show As Human Readable Text
    Create Book Reference
    Go To References List Page
    ${normal}=  Run Keyword And Return Status    Element Should Be Visible   id=view_normal_format
    Run Keyword If    ${normal}    Click Normal Button If Shown   
    Page Should Contain  Book_Kirjoittaja
    Page Should Contain  Editori
    Page Should Contain  Kirjoitus
    Page Should Contain  Publisher
    Page Should Contain    1999
    Page Should Not Contain    Referenssi 1



Created Reference Should Show As BibTex
    Create Book Reference
    Go To References List Page
    ${present}=  Run Keyword And Return Status    Element Should Be Visible   id=view_bibtex_format
    Run Keyword If    ${present}    Click BibTex Button If Shown   
    Page Should Contain    Referenssi 1
    Page Should Contain  Book_Kirjoittaja
    Page Should Contain  Editori
    Page Should Contain  Kirjoitus
    Page Should Contain  Publisher
    Page Should Contain    1999
    

*** Keywords ***
Create Book Reference
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Scroll Element Into View  book_submit
    Click Book Submit
    Main Page Should Be Open

Click BibTex Button If Shown
    Click Button  view_bibtex_format

Click Normal Button If Shown
    Click Button  view_normal_format

Set Name
    [Arguments]  ${name}
    Input Text  xpath=//form[@id='book']//input[@name='name']  ${name}

Set Author
    [Arguments]  ${author}
    Input Text  xpath=//form[@id='book']//input[@name='author']  ${author}

Set Editor
    [Arguments]  ${editor}
    Input Text  xpath=//form[@id='book']//input[@name='editor']  ${editor}

Set Title
    [Arguments]  ${title}
    Input Text  xpath=//form[@id='book']//input[@name='title']  ${title}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  xpath=//form[@id='book']//input[@name='publisher']  ${publisher}

Set Year
    [Arguments]  ${year}
    Input Text  xpath=//form[@id='book']//input[@name='year']  ${year}

Click Book Submit
    Click Button  book_submit

Set Book Information
    Set Name  Referenssi 1
    Set Author  Book_Kirjoittaja
    Set Editor  Editori
    Set Title  Kirjoitus
    Set Publisher  Publisher
    Set Year  1999