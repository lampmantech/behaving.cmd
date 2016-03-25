Feature: Files

  @cmd
  Scenario: Simple starting points, assuming a Unix filesystem

      Giben Ensure the directory "/etc" exists
       Then Ensure the file "/etc/fstab" exists


