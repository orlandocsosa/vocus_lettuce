Feature: Go to careers page
  In order to test Vocus page
  As a user
  I want to go to Vocus careers page

  Scenario: Positive path
    Given I go to "http://www.vocus.com.au/"
    When I click the About Us link in the menu
    And I click the careers link
    Then The browser's URL should be "http://www.vocus.com.au/careers"

