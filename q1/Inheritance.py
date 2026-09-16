# Inheritance

class Vehicle:
    def __init__(self, kindofvehicle):
        self.kindofvehicle = kindofvehicle 
        print(self.kindofvehicle, "created.")
    def move(self, distance):
        print(self.kindofvehicle, "moved", distance, end="")

class Car(Vehicle):
    def __init__(self, kindofvehicle, brand, model):
        super().__init__(kindofvehicle) 
        print("It is a", brand, model)
    def move(self, distance):
        super().move(distance)
        print("KM")

class Boat (Vehicle):
    def __init__(self, kindofvehicle, model):
        super().__init__(kindofvehicle) 
        print("It is a", model)
    def move(self, distance):
        super().move(distance)
        print("NM")
        
weh = Vehicle("carriage") 
weh.move(5)
car = Car("car", "Toyota", "Vios") 
car.move(10)
boat = Boat("boat", "The Boat")
boat.move(15)


