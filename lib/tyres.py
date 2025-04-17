class TyreLog:

    def __init__(self):
        self.tyres_log = []
        self.historical_readings = []

    def add(self, tyre):
        self.tyres_log.append(tyre)

    def tyre_data(self, pressure, depth):
        pass
    
    def list_of_tyres(self):
        return 




class Tyres:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position

    