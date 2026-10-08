# void = function that does not return anything
# yung mga iba (float, int, str) = they just return smth
# yung mga nasa taas sa uml diagram, it's not in the function

class Account:
    name = ""
    number = ""
    __balance = 0
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
    def getBalance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance +=amount
        
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def __str__(self):
        return self.name + " [" + self.number + "] P " + str(self.__balance)
        #need to convert self.__balance to str

    def __del__(self):
        print("Account", self.number, "closed")


class SavingsAccount(Account):
    # you don't need to do the super() stuff for the others bcs it can already access/inherit lahat ng nasa account
    __interest = 0.05
    def addInterest(self): # u add interest
        interestToAdd = super().getBalance() * self.__interest # u cant do __balance since it is private so u do the function
        super().deposit(interestToAdd)
        # uses deposit function to add interest
        
class Bank:
    name = ""
    __accounts = []
    def __init__(self,name):
        self.name = name
        print("Welcome to", self.name)

    def openAccount(self):
        print("Ready to open an account")
        acc_nam = input("Account name:   ")
        acc_num = input("Account number: ")
        acc_typ = input("Account type (savings or checking): ")
        
        # checks whether they created savings or normal acct
        if acc_typ.lower() == "savings":
            account = SavingsAccount(acc_nam, acc_num)
        else:
            account = Account(acc_nam, acc_num)
        print("Account created")
        print(account)
        self.__accounts.append(account)

    def showAccounts(self):
        print("Showing accounts")
        for a in self.__accounts: # shows the accounts
            print(a)  # prints str function

    def deposit(self):
        print("Ready to deposit an amount")
        amount = float(input("Enter amount to deposit: "))
        acc_num = input("Enter account number: ")
        for a in self.__accounts: # checks which account ur gonna deposit in
            if a.number == acc_num:
                a.deposit(amount)
                print("Deposit successful")
                print(a) # prints str function

    def addInterest(self):
        print("Adding interest to all savings accounts")
        for a in self.__accounts:
            if isinstance(a, SavingsAccount):
                a.addInterest()
                print("Interest added to account", a.number)
                print(a) # prints str function

    def closeAccount(self):
        print("Ready to close an account")
        acc_num = input("Enter account number: ")
        for a in self.__accounts: # checks which account ur gonna close
            if a.number == acc_num:
                self.__accounts.remove(a) # removes acct fr. list
                del a # deletes account
                print("Account closed")

    def __del__(self):
        print("Thank you for banking with", self.name)
        for a in self.__accounts: 
            self.__accounts.remove(a)# deletes remaining account
            del a
        
        
mbtc = Bank("Metrobank")
mbtc.openAccount()
mbtc.openAccount()
mbtc.showAccounts()
mbtc.deposit()
mbtc.deposit()
mbtc.addInterest()
mbtc.closeAccount()
del mbtc



