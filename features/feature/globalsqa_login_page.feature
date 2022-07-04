Feature: Globalsqa page
  Scenario: login and create new customer
    Given I launch chrome browser
    When I open globalsqa login page
    Then I click Bank Manager Login button
    Then I click Add customer button
    And I fill all fields and submit
    Then I click Add customer button
    And I search added customer
    Then I delete customer
    And I close browser