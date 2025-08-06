class BankAccount:
    
    #CONSTRUCTOR
    def __init__(self, holder, balance):
        self.__holder = holder
        self.__balance = balance
    
    #GETTERS
    def getHolder(self):
        return self.__holder
    
    def getBalance(self):
        return self.__balance
    
    #SETTERS
    def setHolder(self, holder):
        self.__holder = holder
    
    def setBalance(self, balance):
        self.__balance = balance
    
    #METHODS
    def deposit(self, amount):
        if amount <= 0:
            return "Select a valid value to deposit."
        else:   
            self.__balance += amount
            return "Deposit success."
    
    def withdraw(self, amount):
        if self.__balance < 0 or self.__balance - amount < 0:
            return f"You can't withdraw {amount}, check your balance."
        else:
            self.__balance -= amount
            return "Withdraw success."

    def showBalance(self):
        txt = f"\n------ {self.__holder.upper()} BALANCE ------"
        txt += f"\n{self.__balance}"
        return txt
