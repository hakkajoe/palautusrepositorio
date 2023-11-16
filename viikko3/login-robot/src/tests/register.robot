*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    matti    matti123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    kalle    kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials    ma    matti123
    Output Should Contain  Invalid username

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    123456789    matti123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials    matti    matti1
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    matti    mattimatti
    Output Should Contain  Invalid password

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command