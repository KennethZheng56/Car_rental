from pyscript import document, when

cars = ["Toyota", "Honda", "BMW"]

@when("click", "#view-catalogue")
def hi(event=None):
    # Build an unordered list of cars
    html = "<ul>"
    for car in cars:
        html += f"<li>{car}</li>"
    html += "</ul>"

    # Insert into the <p id="test"> element
    document.getElementById("test").innerHTML = html
