

from abc import ABC, abstractmethod

class Vechile(ABC):
    
    @abstractmethod
    def start_engine(self):
        "Abstract method; no body logic allowed here"
        pass
    
    
class Car(Vechile):
    def __init__(self):
        super().__init__()
    
    def start_engine(self):
        return "Car Engine started smoothly"
    
# vechile = Vechile()  #Raises TypeError! Cannot instantiate abstract class

my_car = Car()
print(my_car.start_engine()) 
    

"""
2. Interfaces in Python
An Interface is a purely structural contract. Unlike some languages (like Java or TypeScript) that have an explicit interface keyword, Python implements interfaces using pure abstract classes (an abstract class where every single method is an @abstractmethod and it holds no data variables)
"""


from abc import ABC, abstractmethod

class DBConnection(ABC):
    @property
    @abstractmethod
    def connect(self):
        # Must be overridden by subclasses
        pass
        
    def log_status(self):
        # Concrete method; shared by all subclasses
        return "Connection log initiated."

class Django(DBConnection):
    def __init__(self):
        super().__init__()
        
    @property
    def connect(self):
        return "Django is trying to connect" 
    # Now you can access this method as any normal attribute.
    

django = Django()
print(django.connect)
print(django.log_status())
