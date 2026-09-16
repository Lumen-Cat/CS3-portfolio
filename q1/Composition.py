# Relationships in Python OOP
# Composition ->
# an object gets built inside the class' constuctor
# When the main object gets deleted, its inner one also disappears

class Mitochondria:
    def __init__(self):
        print("Mitochondria is created")
    def powerTheCell(self):
        print("Mitochondira is providing power to the cell") 
    def __del__(self):
        print("Mitochondria is gone")

class Nucleus:
    def __init__(self):
        print("Nucleus is created")
    def __del__(self):
        print("Nucleus is gone")

class Cell:
    def __init__(self):
        print("Cell is created") 
        self.mitochondria = Mitochondria()
        self.nucleus = Nucleus ()
    def exists(self):
        self.mitochondria.powerTheCell() 
        print("Cell is existing")
    def __del__(self):
        del self.mitochondria 
        del self.nucleus
        print("Cell is deleted")

cellAtWork = Cell() 
cellAtWork.exists() 
del cellAtWork



