from lib.check_TODO_TDD import check_todo

def test_check_todo_empty_string():
    assert check_todo() == False

def test_check_todo_word():
    assert check_todo("word") == False 

def test_check_todo_in_todo():
    assert check_todo("#TODO") == True

def test_check_todo_sentence_with_todo():
    assert check_todo("#TODO buy milk") == True

def test_check_todo_sentence_without_todo():
    assert check_todo("drink tea") == False

def test_check_todo_sentence_with_todo_at_end():
    assert check_todo("learn to test-drive my code #TODO") == True