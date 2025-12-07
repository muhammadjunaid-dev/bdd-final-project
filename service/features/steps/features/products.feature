Feature: Product Management API

  Background:
    Given the following products exist
      | id | name       | category    | available |
      | 1  | Product A  | Category 1 | True      |
      | 2  | Product B  | Category 2 | True      |
      | 3  | Product C  | Category 1 | False     |
      | 4  | Big Mac    | Food       | True      |
      | 5  | Hat        | Clothing   | True      |

  # Task 6a – Reading a Product
  Scenario: Reading a Product
    When I retrieve product with id 1
    Then the product name should be "Product A"

  # Task 6b – Updating a Product
  Scenario: Updating a Product
    When I search for product with name "Product B"
    Then I should see the product details
    When I update the product's name to "Product B Updated"
    Then I should see the message "Success"
    When I retrieve the product with id 2
    Then the product name should be "Product B Updated"

  # Task 6c – Deleting a Product
  Scenario: Deleting a Product
    When I search for product with name "Product C"
    Then I should see the product details
    When I delete the product with id 3
    Then I should see the message "Product has been Deleted!"
    When I search for product with name "Product C"
    Then I should not see the product in results

  # Task 6d – Listing All Products
  Scenario: Listing All Products
    When I clear the form and press the Search button
    Then I should see all products such as "Hat", "Shoes", "Big Mac", "Sheets"

  # Task 6e – Search by Category
  Scenario: Searching a Product by Category
    When I clear the page and select category "Food"
    And I press the Search button
    Then I should see "Big Mac" in results
    And I should not see other foods from Background data

  # Task 6f – Search by Availability
  Scenario: Searching a Product by Availability
    When I set Available dropdown to True
    And I press the Search button
    Then I should see only available items from Background data

  # Task 6g – Search by Name
  Scenario: Searching a Product by Name
    When I set Available dropdown to True
    And I search for product with name "Big Mac"
    Then I should see "Big Mac" in results
    And I should not see unavailable items
