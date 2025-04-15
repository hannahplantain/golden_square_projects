import math

class Diary:
    def __init__(self):
        self.entries = []

    
    def add(self, entry):
        self.entries.append(entry)
        

    def all(self):
        return self.entries

    
    def count_words(self):
        word_counts = [entry.count_words() for entry in self.entries]
        return sum(word_counts)

    def reading_time(self, wpm):
        if self.entries == []:
            raise Exception ("No entries added yet.")
        word_count = self.count_words()
        return math.ceil(word_count / wpm)
    

    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        entries_user_can_read = []
        for entry in self.entries:
            if entry.count_words() <= words_user_can_read:
                entries_user_can_read.append(entry)
        if entries_user_can_read == []:
            return None
        return entries_user_can_read[0]

