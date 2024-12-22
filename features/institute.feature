Feature: Institute Management
  As a Super Admin
  I want to manage educational institutes
  So that I can create new institutes and assign admins

  Scenario: Super Admin creates a new educational institute
    Given the Super Admin is logged in
    When the Super Admin clicks on "Create Institute" button
    And fills in the institute details
    And submits the form
    Then the new educational institute should be created successfully
