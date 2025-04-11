class Music:
    
    def __init__(self):
        self.track_list = []

    def add_tracks(self, track):
        if track not in self.track_list:
            self.track_list.append(track)

    def check_list(self):
        return self.track_list