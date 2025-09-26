class Vehicle:
    name:str
    year:int
    make:str
    mileage:int
    color:str
    location:str
    available:bool
    rent_cost:int
    def __init__(self, name, make, mileage, year, color, location):
        self.name = name
        self.year = year
        self.mileage = mileage
        self.color = color
        self.location = location
        self.available = True
        
    def getAvailable(self):
        return self.available

    def changeAvailable(self):
        self.available = not self.available

    def getInfo(self):
        return [self.name, self.year, self.mileage, self.color, self.location, self.available]
