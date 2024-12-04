*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Database

*** Test Cases ***
Deleting a Reference Should Remove It From The List
    Create Misc Reference
    Go To References List Page
    ${exists}=    Run Keyword And Return Status    Page Should Contain    Referenssi1
    Should Be True    ${exists}    Reference should exist before deletion.
    Delete Reference    Referenssi1
    Go To References List Page
    ${deleted}=  Run Keyword And Return Status    Page Should Contain    Referenssi1
    Should Be False    ${deleted}    Reference should no longer exist after deletion.

*** Keywords ***
Delete Reference
    [Arguments]  ${name}
    Click Button  xpath=//tr[td[contains(text(), '${name}')]]//button[contains(text(), 'Delete')]
    Confirm Deletion

Confirm Deletion
    Wait Until Page Contains Element    xpath=//div[@id='confirmation-dialog']//button[contains(text(), 'Confirm')]
    Click Button    xpath=//div[@id='confirmation-dialog']//button[contains(text(), 'Confirm')]

Create Misc Reference
    Go To New Reference Page
    Select Radio Button  refTypeCheckbox  misc
    Page Should Contain  Creating misc type reference
    Set Misc Information
    Scroll Element Into View  misc_submit
    Click Misc Submit
    Main Page Should Be Open

the delete button:
   def delete_reference(self, reference_id):
        sql = text("""
            DELETE FROM "references"
            WHERE id = :id
        """)
        self.__db.session.execute(sql, {"id": reference_id})
        self.__db.session.commit()