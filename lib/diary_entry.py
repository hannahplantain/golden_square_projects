import math

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title   #   title: string
        self.contents = contents   #   contents: string
        self.read_so_far = 0
        pass

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents_words())   #   int: the number of words in the diary entry

    def reading_time(self, wpm):
        minutes = math.ceil(len(self.contents_words()) // wpm)
        return minutes

    def reading_chunk(self, wpm, minutes):

        words_user_can_read = wpm * minutes
        words = self.contents_words()
        if self.read_so_far >= len(words):
            self.read_so_far = 0
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_user_can_read
        chunk_words = words[chunk_start : chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk_words)
    
    def contents_words(self):
        return self.contents.split()


# entry = DiaryEntry("First Entry", "This should be a long sentence and take awhile to read.")
# print(entry.reading_chunk(2, 2))
# print(entry.reading_chunk(2, 3))
# print(entry.reading_chunk(2, 2))
# print(entry.reading_chunk(2, 2))