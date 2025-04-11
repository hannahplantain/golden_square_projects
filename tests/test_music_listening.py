from lib.music_listening import *


"""
Given a name 
#returns none for an empty track list
"""

def test_returns_empty_track_list():
    music = Music()
    assert music.check_list() == []

"""
Given a name and a track
#returns the track list with 1 track
"""

def test_add_one_track_return_one_track():
    music = Music()
    music.add_tracks("Show me love")
    assert music.check_list() == ["Show me love"]
"""
Given a name and multiple tracks
#returns a list with the multiple tracks
"""

def test_add_multiple_tracks_return_tracks():
    music = Music()
    music.add_tracks("Show me love")
    music.add_tracks("Birds of a feather")
    assert music.check_list() == ["Show me love", "Birds of a feather"]
"""
Given a name and duplicate tracks
#returns a list without the duplicate track added
"""

def test_add_duplicate_tracks_return_original_list():
    music = Music()
    music.add_tracks("Show me love")
    music.add_tracks("Birds of a feather")
    music.add_tracks("Show me love")
    assert music.check_list() == ["Show me love", "Birds of a feather"]
