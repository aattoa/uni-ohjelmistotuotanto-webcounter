*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Start Fresh

*** Test Cases ***
Set the counter to an arbitrary value
    Fill Text  id=new_value  314159
    Click  button >> text=Aseta
    Get Text  body  contains  nappia painettu 314159 kertaa
