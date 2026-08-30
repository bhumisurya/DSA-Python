class bank():
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        if amount > 0: 
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

a = bank(10000)
a.deposite(4500)
a.withdraw(3300)

print(a.get_balance())