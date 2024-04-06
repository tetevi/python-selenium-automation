# Created by tetev at 4/5/2024
#Feature: Verify “Your cart is empty” Test
#
#  Scenario: User verifies cart is empty
#    Given Open Target main page
#    When Click Cart icon
#    Then Verify cart is empty


Feature: Verify Sign In page Test

  Scenario: User verifies that sign In page is accessible
    Given Open Target main page
    When Click Sign In
    When Click Sign In from nav menu
    Then Verify Sign In form opened