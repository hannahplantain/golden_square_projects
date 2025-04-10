class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title   #   title: string
        self.contents = contents   #   contents: string
        pass

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents.split())   #   int: the number of words in the diary entry

    def reading_time(self, wpm):
        minutes = len(self.contents.split()) // wpm
        if minutes == 0:
            return f"This text will take you less than 1 minute to read"
        elif minutes == 1:
            return f"This text will take you approximately {minutes} minute to read"
        else:
            return f"This text will take you approximately {minutes} minutes to read"

    def reading_chunk(self, wpm, minutes):
        total_minutes = len(self.contents.split()) // wpm
        return 
    #     # Parameters
    #     #   wpm: an integer representing the number of words the user can read
    #     #        per minute
    #     #   minutes: an integer representing the number of minutes the user has
    #     #            to read
    #     # Returns:
    #     #   string: a chunk of the contents that the user could read in the
    #     #           given number of minutes
    #     #
    #     # If called again, `reading_chunk` should return the next chunk,
    #     # skipping what has already been read, until the contents is fully read.
    #     # The next call after that should restart from the beginning.
    #     pass
