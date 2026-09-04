class Technician:
    name = ""
    assigned_lab = None
    def __init__(self,name):
        self.name = name
        
    def assign_lab(self, lab_obj):
        self.assigned_lab = lab_obj

class Lab:
    room_number = ""
    def __init__(self,room_number):
        self.room_number = room_number
        
        
chem_lab = Lab("302")
mr_cruz = Technician("Mr. Cruz")
mr_cruz.assign_lab(chem_lab)
print(mr_cruz.assigned_lab.room_number)



