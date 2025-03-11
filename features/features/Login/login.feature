@login
Feature: Login

  Scenario Outline: User should be able to login
    #Given the user is on the account page
    When  User Enters A Username <Username>
    And   User Enters A Password <Password>
    And   User Clicks On Continue Button
    Then  User Should Be Logged In

    Examples:
      | Username | Password |
      | MASKED   | MASKED   |
