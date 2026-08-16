
class BankAccount():
    def __init__(self, name, balance, age):
        self.name = name
        self.__balance = balance
        self.__age = age
    
    @property
    def balance(self):
        # Getter(@property) : Helps to read the private property like a normal attribute.
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        """Setter: Intercepts changes to validate the data first."""
        if amount < 0:
            raise ValueError("Balance can not be negative!")
        
        self.__balance = amount
    
    def get_age(self):
        return self.__age   

account = BankAccount("Anish", 34000, 22)
print(account.balance)
print(account.name)

# account.balance = 1500
# account.balance = -50  #raises an Value error
account.balance += 1500

print(account.balance)

# trying to obtain private value
# print(account.__age)  
# gives an atttribute error.

# To get it, get it from a method.
print(account.get_age())

