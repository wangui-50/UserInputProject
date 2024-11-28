# Base class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement the move method")

# Derived class: Car
class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving on the road 🚗."

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying in the sky ✈."

# Derived class: Boat
class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing on the water 🚤."

# Derived class: Bicycle
class Bicycle(Vehicle):
    def move(self):
        return f"{self.name} is pedaling along the path 🚴."

# Main program demonstrating polymorphism
if __name__ == "__main__":
    # List of different vehicle objects
    vehicles = [
        Car("Toyota"),
        Plane("Boeing 747"),
        Boat("Yacht"),
        Bicycle("Mountain Bike"),
    ]

    # Loop through the list and call the move method for each
    for vehicle in vehicles:
        print(vehicle.move())