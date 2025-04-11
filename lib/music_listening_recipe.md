
## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

```python
# EXAMPLE

class Music:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   name: none
        # Side effects:
        #   contains a list of saved tracks
        pass # No code here yet

    def add_tracks(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves listened to tracks in a list
        pass # No code here yet

    def check_list(self):
        # Returns:
        #   A list containing added tracks
        # Side-effects:
        #   If there are no tracks in the list, returns none
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name 
#returns none for an empty track list
"""
music = Music()
music.check_list()# => None

"""
Given a name and a track
#returns the track list with 1 track
"""
music = Music()
music.add_tracks("Show me love")
music.check_list() # => ["Show me love"]
"""
Given a name and multiple tracks
#returns a list with the multiple tracks
"""
music = Music()
music.add_tracks("Show me love")
music.add_tracks("Birds of a feather")
music.check_list() # => ["Show me love", "Birds of a feather"]
"""
Given a name and duplicate tracks
#returns a list without the duplicate track added
"""
music = Music()
music.add_tracks("Show me love")
music.add_tracks("Birds of a feather")
music.add_tracks("Show me love")
music.check_list() # => ["Show me love", "Birds of a feather"]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
