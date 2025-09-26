from pyscript import document, when
import json

DB_KEY_USERS = "temp_users"
DB_KEY_CARS = "temp_cars"

DEFAULT_USERS = [
    {"username": "Matthew_Liao", "password": "IS_GAY", "role": "admin"},
    {"username": "Homer", "password": "Wang", "role": "user"}
]

DEFAULT_CARS = ["Toyota", "Honda", "BMW"]

def load_cars():
    cars_json = document.window.localStorage.getItem(DB_KEY_CARS)
    if cars_json is None:
        save_cars(DEFAULT_CARS)
        return DEFAULT_CARS
    return json.loads(cars_json)

def save_cars(cars):
    document.window.localStorage.setItem(DB_KEY_CARS, json.dumps(cars))

def add_car(car):
    cars = load_cars()
    if car not in cars:
        cars.append(car)
        save_cars(cars)

def remove_car(car):
    cars = load_cars()
    if car in cars:
        cars.remove(car)
        save_cars(cars)

cars = load_cars()

@when("click", "#view-catalogue")
def show_cars(event=None):
    html = "<ul>"
    for car in cars:
        html += f"<li>{car}</li>"
    html += "</ul>"
    document.getElementById("test").innerHTML = html

# ---- User database ----
def load_db():
    users_json = document.window.localStorage.getItem(DB_KEY_USERS)
    if users_json is None:
        save_db(DEFAULT_USERS)
        return DEFAULT_USERS
    return json.loads(users_json)

def save_db(users):
    document.window.localStorage.setItem(DB_KEY_USERS, json.dumps(users))

def get_users():
    return load_db()

def add_user(username, password, role="user"):
    users = load_db()
    if any(u["username"] == username for u in users):
        return False
    users.append({"username": username, "password": password, "role": role})
    save_db(users)
    return True

def remove_user(username):
    users = load_db()
    users = [u for u in users if u["username"] != username]
    save_db(users)
    return True

def change_role(username, role):
    users = load_db()
    for u in users:
        if u["username"] == username:
            u["role"] = role
            save_db(users)
            return True
    return False

def verify_user(username, password):
    users = load_db()
    for u in users:
        if u["username"] == username and u["password"] == password:
            return u
    return None
