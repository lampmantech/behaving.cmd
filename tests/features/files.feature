Feature: Files

  @cmd
  Scenario: Simple starting points, assuming a Unix filesystem

      Given Assert the directory "/etc" exists
       Then Assert the file "/etc/fstab" exists


