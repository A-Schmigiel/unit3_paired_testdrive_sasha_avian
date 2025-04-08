# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

```python
def includes_todo(str):
    # returns boolean T or F, depending on if '#TODO' is in the string
```
paramaters: takes one string as arguments
returns: one boolean value
side effects: none

## 3. Create Examples as Tests

Function examples:
>>> includes_todo("#TODO buy milk")
True
>>> includes_todo("drink tea")
False
>>> includes_todo("learn to test-drive my code #TODO")
True


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
