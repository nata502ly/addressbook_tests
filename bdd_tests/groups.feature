Feature: Contact group CRUD
  Description

  Scenario Outline: Add new group
    Given a group list
    Given a new group with <name>, <header>, <footer>
    When I add this group to the list
    Then a new group list is equal to the old list with this new group

    Examples:
    | name         | header     | footer |
    | qwrqsdDSA    | New header | sdgsgs |
    | 124%^%^}{    | &^%&^$^%   | 654565 |
    | Новая группа | вапывапыып | ієпара |

  Scenario: Delete a random group
    Given a non-empty group list
    Given a random group
    When I delete this group
    Then a new list is equal to old list without this group