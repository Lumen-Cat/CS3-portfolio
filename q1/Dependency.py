# Relationships in Python OOP
# Dependency ->
# An object can get associated with another for a one-time use Nag-gamitan kayo
# One object could not care less if the other disappears

class Tusoktusok:
    sauce = None
    def __init__(self, name):
        self.name = name
    def dip(self, sauce):
        self.sauce = sauce
    def eat(self):
        #print("I am eating", self.name, "with", self.sauce.name, "and it tastes", self.sauce.taste) 
        print("I am eating", self.name)
        if self.sauce != None:
            print("It was dipped in", self.sauce.name, "and it tastes", self.sauce.taste)
            
class Sauce:
    def __init__(self, name, taste) 
        self.name = name
        self.taste = taste
    def __del__(self):
        print("Ay natapon ang", self.name, "Wala na tuloy")

fishball = Tusoktusok ("fishball")
vinegar = Sauce("vinegar", "sour")
fishball.dip(vinegar)
fishball.eat()
kikiam = Tusoktusok("kikiam")
kikiam.eat()
del vinegar