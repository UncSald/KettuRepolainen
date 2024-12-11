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

When Book Is Submitted Page Should Redirect To References
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Scroll Element Into View  book_submit
    Click Book Submit
    References Page Should Be Open

When Posting Book Without Publisher Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Clear Element Text  xpath=//form[@id='book']//input[@name='publisher']
    Scroll Element Into View  book_submit
    Click Book Submit
    Page Should Contain  Creating book type reference

When Posting Book Without Author Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Clear Element Text  xpath=//form[@id='book']//input[@name='author']
    Scroll Element Into View  book_submit
    Click Book Submit
    Page Should Contain  Creating book type reference

When Book Is Submitted Correct Pages Format Should Redirect To References
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Set Pages  39-70
    Scroll Element Into View  book_submit
    Click Book Submit
    References Page Should Be Open

When Posting Book With Wrong Pages Format Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Clear Element Text  xpath=//form[@id='book']//input[@name='pages']
    Set Pages  1-
    Scroll Element Into View  book_submit
    Click Book Submit
    Page Should Contain  Creating book type reference

When Posting Book With Wrong Fromat Of Keyword Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Clear Element Text  xpath=//form[@id='book']//input[@name='name']
    Set Name  New Name
    Scroll Element Into View  book_submit
    Click Book Submit
    Page Should Contain  Creating book type reference

When Posting Book With Wrong Fromat Of Author Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Clear Element Text  xpath=//form[@id='book']//input[@name='author']
    Set Author  New-Author+
    Scroll Element Into View  book_submit
    Click Book Submit
    Page Should Contain  Creating book type reference

When Posting Book With Wrong Fromat Of Editor Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Clear Element Text  xpath=//form[@id='book']//input[@name='editor']
    Set Editor  New-Editor+
    Scroll Element Into View  book_submit
    Click Book Submit
    Page Should Contain  Creating book type reference

When Posting Book With Wrong Fromat Of Title Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Clear Element Text  xpath=//form[@id='book']//input[@name='title']
    Set Title  New-Title+
    Scroll Element Into View  book_submit
    Click Book Submit
    Page Should Contain  Creating book type reference

When Posting Book With Wrong Fromat Of Year Error Is shown
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  book
    Page Should Contain  Creating book type reference
    Set Book Information
    Clear Element Text  xpath=//form[@id='book']//input[@name='year']
    Set Year  12
    Scroll Element Into View  book_submit
    Click Book Submit
    Page Should Contain  Creating book type reference    


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

Set Pages
    [Arguments]  ${pages}
    Input Text  xpath=//form[@id='book']//input[@name='pages']  ${pages}

Click Book Submit
    Click Button  book_submit

Set Book Information
    Set Name  Referenssi1
    Set Author  Kirjoittaja
    Set Editor  Editori
    Set Title  Kirjoitus
    Set Publisher  Publisher
    Set Year  1999