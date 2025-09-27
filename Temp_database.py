from pyscript import document, when, display
from js import window
from Vehicle import Vehicle
import json

DB_KEY_CARS = "temp_cars"

# Load cars from localStorage or set default list
def load_cars():
    cars_json = window.localStorage.getItem(DB_KEY_CARS)
    if cars_json is None or cars_json == "null":
        toyota = Vehicle("Toyota", "make", "1000", "2019", "red", "351").to_dict()
        honda = Vehicle("Honda", "make", "1000", "2019", "red", "351").to_dict()
        bmw = Vehicle("BMW", "make", "1000", "2019", "red", "351").to_dict()
        cars = [toyota, honda, bmw]
        save_cars(cars)
        return cars
    try:
        return json.loads(str(cars_json))
    except json.JSONDecodeError:
        toyota = Vehicle("Toyota", "make", "1000", "2019", "red", "351").to_dict()
        honda = Vehicle("Honda", "make", "1000", "2019", "red", "351").to_dict()
        bmw = Vehicle("BMW", "make", "1000", "2019", "red", "351").to_dict()
        cars = [toyota, honda, bmw]
        save_cars(cars)
        return cars

# Save cars to localStorage
def save_cars(cars):
    window.localStorage.setItem(DB_KEY_CARS, json.dumps(cars))

# Get current car list
# toyota = Vehicle("Toyota", "make", "1000", "2019", "red", "351").to_dict()
# save_cars([toyota])
cars = load_cars()

# Button handler to show catalogue
@when("click", "#view-catalogue")
def show_cars(event=None):
    html = "<ul>"
    l1 = []
    hidden = ""
    book = "<button> Book This Car </button>"
    for car in cars:
        name = car['name']
        l1.append(name)
        html += f"<li id='toggle_{name}' >{name}"
        # hides the car info (remove brackets around 'hidden' to hide it)
        html += f"<ul class={hidden} id={str(name)}>"
        # Adds the other car info 
        for k in car.keys():
            if k != 'name':
                html += f"<li>{k.capitalize()}: {car[k]}</li>"
        html += f"</ul>{book}</li>"
    html += "</ul>"
    #vvv-this thing is supposed to make the visibility toggable-vvv
    html += js_code(l1)
    document.getElementById("test").innerHTML = html

# Doesn't work btw vvv
def js_code(id:list[str]):
    code = """
    <script> 
    """
    for i in id:
        code += f"""
        console.log("bye");
        
        const toggle = document.getElementById('toggle_{i}');
        const thing = document.getElementById('{i}');
        toggle.addEventListener("click", ()=> {'{'}
            console.log("no");
            if (thing.style.display == 'none' || thing.style.display == '') {'{'}
                thing.style.display = 'block';
            {'}'} else {'{'} thing.style.display = 'none';{'}'}
            {'}'})
        {'}'}
        """
    code += "</script>"
    return code
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
