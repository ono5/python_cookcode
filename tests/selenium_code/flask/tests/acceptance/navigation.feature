Feature: Test navigation between pages
  We can have a longer description
  That can span a fea lines

  Scenario: Homepage can go to Blog
    Given I am on the homepage
    When I click on the link with id "blog-link"
    Then I am on the blog page
