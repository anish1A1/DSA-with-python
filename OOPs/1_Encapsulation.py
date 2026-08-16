
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



class Calculator():
    def __init__(self):
        self.result = 0
    
    def __validate(self, nums):
        if not isinstance(nums, (int, float)):
            # isInstance will check the object's value if it is int/float or not.
            return False
        return True
    
    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid Number. Retry!")
    
calc = Calculator()
calc.add(5)

print(calc.result)
calc.add(15)
print(calc.result)

# When accessing private method will give an error
# print(calc.__validate)

calc.add('s')
print(calc.result)


# We can also do encapsulation without @property decorator

# Method 1: Traditional Getter and Setter Methods (Java Style)You write explicit, separate methods to get and set the value. You must call these methods using parentheses ().pythonclass Wallet:

class Wallet:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    # Explicit Getter method
    def get_balance(self):
        return self.__balance

    # Explicit Setter method
    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount

# Usage
obj = Wallet(100)
obj.set_balance(150)         # Must call as a function cannot call __balance as done with @property
print(obj.get_balance())     # Output: 150
# print(obj.__balance) #Error