#Francesca Scippa
#08-05-2024
#senza test!

from ANIMALS import Animal
from FENCE import Fence
from ZOOKEEPER import ZooKeeper

class Zoo:
    
    def __init__(self, fance: list[Fence], animals: list[Animal], guardians: list[ZooKeeper]):
        
        self.fance: list[Fence] = fance
        self.animals: list[Animal] = animals
        self.guardians: list[ZooKeeper] = guardians
    
    def __str__(self):
        return f"Fances: {self.fance}\nAnimals: {self.animals}\nGuardians: {self.guardians}"
        
   # def describe_zoo(self):
       # return __str__()