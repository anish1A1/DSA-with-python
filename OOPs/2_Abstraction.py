

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
    
