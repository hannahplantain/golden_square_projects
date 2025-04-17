class MasterDiary:

    def __init__(self):
        self.secret_diary = []
        self.todo_list = []
        self.phone_book = []

    def add_diary_entry(self, entry):
        self.secret_diary.append(entry)
    
    def read_past_entry(self, entry):
        return entry.format()

    
    def read_time_efficient_entry(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        entries_user_can_read = []
        for entry in self.secret_diary:
            if entry.count_words() <= words_user_can_read:
                entries_user_can_read.append(entry)
        if entries_user_can_read == []:
            return None
        return entries_user_can_read[0]

    def add_todo_entry(self, todo):
        self.todo_list.append(todo)
    
    def list_of_contact_numbers(self):
        for entry in self.secret_diary:
            self.phone_book.extend(entry.extract_phone_numbers())
        return self.phone_book
        

        
class DiaryEntries:

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        return len(self.contents.split())
    
    def extract_phone_numbers(self):
        import re
        return re.findall(r'\b0[0-9]{10}\b', self.contents)


class TodoEntries:

    def __init__(self, todo):
        self.todo = todo


