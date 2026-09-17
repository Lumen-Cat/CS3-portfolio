
class Glassware:
    def __init__(self,kind):
        self.kind = kind
    
class Beaker(Glassware):
    def __init__(self,kind,name):
        super().__init__(kind)
        self.name = name
        print(f"Name of {kind}: {name}")
        
    def __del__(self):
        print(end="")
        
class Tray:
    def __init__(self):
        print("Tray exists.\n")
        
    def seeContents(self):
        self.contents = [Beaker("Beaker", s) for s in range(1,6)]
    
    def __del__(self):
        print("\nTray is disposed.")
        print (f"Deleting all beakers.")
        del self.contents
        #del 
    
organizedTray = Tray()
organizedTray.seeContents()
del organizedTray