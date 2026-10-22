class Patient:
    __name = ""
    __bill_amount = float(0)

    def __init__(self,name,bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name


    def set_name(self,name):
        self.__name = name


    def get_bill_amount(self):
        return self.__bill_amount


    def set_bill_amount(self,bill_amount):
        self.__bill_amount = bill_amount


    def calculate_bill(self):
        bill = self.__bill_amount
        return bill

    def display_info(self):
        print(f"Patient Name: {self.__name}")
        print(f"Original Bill: {float(self.__bill_amount)}")
        print(f"Final Bill: {float(self.calculate_bill())}\n")

        
class SeniorPatient(Patient):
    def calculate_bill(self):
        bill = super().get_bill_amount() - 0.20*super().get_bill_amount()
        return bill


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        bill = super().get_bill_amount() - 0.15*super().get_bill_amount()
        return bill


print("Hospital Billing System")
print("-------------------------")

regularPatient = Patient("Juan Dela Cruz", 15000)
regularPatient.display_info()

seniorPatient = SeniorPatient("Maria Santos", 15000)
seniorPatient.display_info()

philHealthPatient = PhilHealthPatient("Pedro Reyes", 15000)
philHealthPatient.display_info()





    
