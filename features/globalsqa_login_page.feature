Feature: Globalsqa page
  Scenario: login and create new customer
    Given launch chrome browser
    When open globalsqa login page
    Then click Bank Manager Login button
    Then click Add customer button
    And fill all fields and submit
    Then click Add customer button
    And search added customer
    Then delete customer
    And close browser