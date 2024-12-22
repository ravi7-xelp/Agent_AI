Feature: Admin interacts with the Chatbot

  Scenario: Admin sends a question to the Chatbot
    Given Admin is logged into the application
    When Admin clicks on an institute from the institutes page
    And Admin navigates to the Chatbot page
    Then Enter the Question in the chat bot field and send
