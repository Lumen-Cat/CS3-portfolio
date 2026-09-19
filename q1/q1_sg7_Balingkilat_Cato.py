
class Glassware:
    def __init__(self,kind):
        self.kind = kind
    
class Beaker(Glassware):
    def __init__(self,kind,brand):
        super().__init__(kind)
        self.brand = brand
        
    def __del__(self):
        print(end="")
        
        
class Tray:
    def __init__(self):
        print("Tray exists.\n")
        self.contents = [
                Beaker("Beaker", "Pyrex"),
                Beaker("Beaker", "Pyrex"),
                Beaker("Beaker", "Pyrex"),
                Beaker("Beaker", "Pyrex"),
                Beaker("Beaker", "Pyrex")
                ]
        
    def seeContents(self):
        for a,b in enumerate(self.contents, 1):
            print(f"Beaker {a}   Brand: {b.brand}")
        
    def __del__(self):
        print("\nTray is disposed.")
        print (f"Deleting all beakers.")
        del self.contents


organizedTray = Tray()
organizedTray.seeContents()
del organizedTray