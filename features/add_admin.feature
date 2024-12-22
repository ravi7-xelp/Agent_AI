Feature: Create Institute Admin

  Scenario: Super Admin creates an institute admin through the settings
    Given the Super Admin is logged into the application with valid credentials
    When the Super Admin select and click institute from the institutes page
    And admin navigates to the metrics page
    And clicks on the settings
    And click on the create admin button
    Then fill create and form and submit
