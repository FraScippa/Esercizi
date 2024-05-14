#Francesca Scippa
#08-05-2024

from ANIMALS import Animal
from FENCE import Fence
from ZOOKEEPER import ZooKeeper

class Zoo:
    
    def __init__(self, fance: list[Fence], animals: list[Animal], guardians: list[ZooKeeper]):
        
        self.fance: list[Fence] = fance
        self.animals: list[Animal] = animals
        self.guardians: list[ZooKeeper] = guardians
    
    def __str__(self):
        print(f"Guardians:\n{self.guardians}\nFances:\n{self.fance}\nwith animals:\n{self.animals}\n")
        
    def describe_zoo(self):
        return self.__str__()