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
   
    def remove_animal(self, animal: Animal, fence: Fence):
        fence.animals.remove(animal.species)
    
    def add_animal(self, animal: Animal, fence: Fence):
        
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
            print("### Wrong input order! The second parament doesn't have an area! ###")
        
    def feed(self, animal: Animal, fence: Fence=None):
        
        if animal.healt != 100 and animal.dimention < fence.area:
            animal.healt += (animal.healt*0.01)
            animal.dimention += (animal.dimention*0.02)
            print(f"health:{animal.healt}\naniml_dimention:{animal.dimention}")
        elif animal.healt == 100:
            print("Your animal is full health!")
        elif animal.dimention > fence.area:
            print("### OH NO!In this fence there is no more space!! ###")

    #def clean(self, fance : Fence) -> float: #Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto.
    
    
    def __str__(self) -> str:
        return f"\nZooKeeper: {self.name} {self.surname}\nID: {self.ID}\n"+"_"*30