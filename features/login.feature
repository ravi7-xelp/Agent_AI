Feature: Super Admin Login, Logout and Navigation

 Scenario: Super Admin logs out successfully
    Given the Super Admin is on the login page
    When the Super Admin enters valid credentials
    And the Super Admin should be redirected to the institutes page
    When the user click on Logout
    Then Redirected to Login page

  Scenario: Super Admin logs in with valid credentials and navigates to the institutes page
  Given the Super Admin is on the login page
  When the Super Admin enters valid credentials
  And the Super Admin should be redirected to the institutes page
  And the user click on Logout



Scenario: Super Admin fails to log in with invalid credentials
    Given the Super Admin is on the login page
    When the Super Admin enters invalid credentials
    Then the login should fail and an error message should be displayed
