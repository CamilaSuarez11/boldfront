Feature: Text Box form submission

  Scenario: User fills in the form with valid data
    Given the user is on the Text Box page
    When the user fills in the form with valid data
    Then the user should see the correct submitted values

  Scenario: User submits the form with some fields missing
    Given the user is on the Text Box page
    When the user fills in the form with some fields missing
    Then the user should see the filled fields in the output container

  Scenario: User submits the form with empty fields
    Given the user is on the Text Box page
    When the user fills in the form with empty fields
    Then the user should not see the output container if all fields are empty

  Scenario: User submits only one field filled
    Given the user is on the Text Box page
    When the user fills in the form with only one field filled
    Then the user should see only the filled field in the output container
