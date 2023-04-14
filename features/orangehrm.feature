
Feature: OrangeHRM Login

    Scenario:login to orangehrm and create employee table
     Given  the user logs in to the application
       | username | password |
       | Admin    | admin123 |
      When  fill the employee details
        | firstname | middlename | lastname |
        | Indraja   |    k       |   u      |
      Then the user details are recorded successfully
