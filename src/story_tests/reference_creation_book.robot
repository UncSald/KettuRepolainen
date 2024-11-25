*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database

*** Test Cases ***
When book form is selected book form is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference

When Book Is Submitted Page Should Redirect To Main
    Go To New Reference Page
    sleep  2s
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    sleep  2s
    Click Book Submit
    Main Page Should Be Open

When Posting Book Without Publisher Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Clear Element Text  xpath=//form[@id='book']//input[@name='publisher']
    Click Book Submit
    Page Should Contain  Publisher is required

When Posting Book Without Author Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Clear Element Text  xpath=//form[@id='book']//input[@name='year']
    Set Year  kaksi
    Click Book Submit
    Page Should Contain  Year must be a number
    

*** Keywords ***
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
    Click Button  xpath=//form[@id='book']//button[@name='book_submit']

Set Book Information
    Set Name  Referenssi 1
    Set Author  Kirjoittaja
    Set Editor  Editori
    Set Title  Kirjoitus
    Set Publisher  Publisher
    Set Year  1999