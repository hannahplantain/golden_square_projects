# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_todo(string):
    """returns True if #TODO in string

    Parameters: (list all parameters and their types)
        string: a string containing tasks (e.g. "#TODO wash dishes")

    Returns: (state the return value and its type)
        True or False

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given input "#TODO buy milk" returns True
"""
check_todo("#TODO buy milk") => True

"""
Given input "drink tea" returns False

"""
check_todo("drink tea") => False

"""
Given input "learn to test-drive my code #TODO" returns False

"""
check_todo("learn to test-drive my code #TODO") => True

"""
Given an empty string returns False
"""
check_todo("") => False

"""
```

_Encode each example as a test. You can add to the above list as you go._

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
