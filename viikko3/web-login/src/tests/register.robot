*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username    kallekakkonen
    Set Password  kalle123
    Set Password Confirmation    kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation    kalle123
    Submit Credentials
    Register Should Fail With Message    Invalid username

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  123456789
    Set Password Confirmation    123456789
    Submit Credentials
    Register Should Fail With Message    Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation    kalle1234
    Submit Credentials
    Register Should Fail With Message    Passwords do not match

Login After Successful Registration
    Set Username    kallekolmonen
    Set Password  kalle123
    Set Password Confirmation    kalle123
    Submit Credentials
    Go To Login Page
    Set Username  kallekolmonen
    Set Password  kalle123
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Set Username    ka
    Set Password  kalle123
    Set Password Confirmation    kalle123
    Submit Credentials
    Go To Login Page
    Set Username  ka
    Set Password  kalle123
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Register Should Succeed
    Main Page After Registration Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Credentials Login
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password    password    ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password    password_confirmation    ${password_confirmation}