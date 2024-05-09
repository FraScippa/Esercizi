from ANIMALS import Animal
from FENCE import Fence

class ZooKeeper:

    def __init__(self, name: str, surname: str, ID: str):
        
        self.name: str = name
        self.surname: str = surname
        self.ID: str = ID
        if self.ID[0] == '0':
            self.ID = ID[1:]
            self.ID = int(ID)
        else:
            self.ID: int = ID
   
    def remove_animal(self, fence: Fence, *animal: Animal):
        fence.animals.remove(animal.species)
    
    def add_animal(self, fence: Fence, animal: Animal):
        if not isinstance(fence, Fence):
            print("### Type mismatch: 'fence' type not supported ###")
        if not isinstance(animal, Animal):
            print("### Type mismatch: 'animal' type not supported ###")
        try:
            if fence.area > animal.dimention:
                fence.animals.append(animal.species)
            else:
                print("#### OH NO! Your fence is full! Remove an\some animal\s! ###")
        except AttributeError:
            print("### Wrong input order! The first parament doesn't have an area! ###")
        
    #def feed(self, animal: Animal):
        #health += 1
        #height-wheight +2%
        #healt += 1

    def clean(self, fance : Fence) -> float: #Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto.
        if fance in self.fance:
            self.fance: int = 0
    
    def __str__(self) -> str:
        return f"\nZooKeeper: {self.name} {self.surname}\nID: {self.ID}\n"+"_"*30