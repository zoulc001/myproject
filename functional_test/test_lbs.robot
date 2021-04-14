*** Settings ***
Library	test_lbs.py

*** Test Cases ***
test_lbs
    ${res}=    get_lbs_content
    Should Contain    ${res}    Hello world
    
