from pyscript import document

login = [{"username":"Matthew_Liao", "password":"IS_GAY"}]
cars = [{"car":"Honda", "make":"wow", "model":"no", "year":"old"}]

def add_user(user:str, password:str):
  login.append({"username":user, "password":password})

def hi():
  document.getElementById("test").innerText = str(cars)
