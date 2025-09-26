from pyscript import document, when
from js import window
from Vehicle import Vehicle
import json

DB_KEY_CARS = "temp_cars"

# Load cars from localStorage or set default list
def load_cars():
    cars_json = window.localStorage.getItem(DB_KEY_CARS)
    if cars_json is None or cars_json == "null":
        cars = ["Toyota", "Honda", "BMW"]
        save_cars(cars)
        return cars
    return json.loads(str(cars_json))

# Save cars to localStorage
def save_cars(cars):
    window.localStorage.setItem(DB_KEY_CARS, json.dumps(cars))

# Get current car list
cars = load_cars()

# Button handler to show catalogue
@when("click", "#view-catalogue")
def show_cars(event=None):
    html = "<ul>"
    for car in cars:
        html += f"<li>{car}</li>"
    html += "</ul>"
    document.getElementById("test").innerHTML = html

#class Vehicle:
    # name:str
    # year:int
    # make:str
    # mileage:int
    # color:str
    # location:str
    # available:bool
    # rent_cost:int
    # def __init__(self, name, make, mileage, year, color, location):
    #     self.name = name
    #     self.year = year
    #     self.mileage = mileage
    #     self.color = color
    #     self.location = location
    #     self.available = true
        
    # def getAvailable():
    #     return available

    # def changeAvailable():
    #     available = not available

    # def getInfo():
    #     return [name, year, mileage, color, location, true]
