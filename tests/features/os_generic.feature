Feature: Generic OS

  Scenario: These should work on any OS as the tests use Python commands.

      Given I sleep for "5" seconds
       Then Assert the directory "/tmp" exists
        And Ensure that the directory "/tmp/foobar" exists
        And Assert that the directory "/tmp/foobar" exists

