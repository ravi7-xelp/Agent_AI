Feature: Configuration access and API key setup

  Scenario: Super Admin accesses configuration page after navigating through institutes
    Given the Super Admin is logged into the application
    When the Super Admin clicks on an institute from the institutes page
    And navigates to the metrics page
    And clicks on the configuration option
    Then the configuration page should display the required fields:
      | Field Name            |
      | Pinecone API Key      |
      | ChatGPT API Key       |
      | JINA TOKEN            |
      | Supabase Key          |
    And the Save button should be visible
