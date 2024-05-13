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
   
    def add_animal(self, animal: Animal, fence: Fence):
        
        if not isinstance(fence, Fence):
            print("### Type mismatch: 'fence' type not supported ###")
        if not isinstance(animal, Animal):
            print("### Type mismatch: 'animal' type not supported ###")
        
        if animal.preferred_habitat.title() != fence.habitat:
            print(f"### {animal.species}: This animal is not appropiriate for {fence.habitat}. ###")
        
        try:
            if fence.area > animal.dimention:
                fence.area -= animal.dimention
                fence.animals.append(animal)
                
            else:
                print("#### OH NO! Your fence is full! Remove an\some animal\s! ###")
        except AttributeError:
            print("### Wrong input order! The second parament doesn't have an area! ###")
        
    def remove_animal(self, animal: Animal, fence: Fence):
        fence.area += animal.dimention
        fence.animals.remove(animal)
        
    def feed(self, animal: Animal):
        if animal.health != 100:
            if animal.dimention < self.fence.get_area():
                animal.health *= 1.01  
                animal.dimention *= 1.02  
                print(f"Health: {animal.health}\nAnimal Dimension: {animal.dimension}")
            else:
                print("### OH NO! In this fence there is no more space to feed the animal!! ###")
        else:
            print("Your animal is full health!")
            
    def get_animal_species(self, species_name, animals: Fence):
        for animal in animals:
            if animal.species == species_name:
                return animal
        return None
    
    def clean(self, fence : Fence) -> float: 
        total_dimention = 0
        animal = None
        
        for species_name in fence.animals:
            animal = self.get_animal_species(species_name, fence.animals)
            if animal is not None:
                total_dimention += animal.get_dimention()
        
        if total_dimention == 0:
            cleaning_time = fence.area
        else:
            empty_area = fence.area - total_dimention
            
            if empty_area == 0:
                cleaning_time = total_dimention
            else:
                cleaning_time = fence.area / empty_area

        fence.animals.clear()
        print(f'The cleaning time is: {cleaning_time}')
            
        

    #Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto.
    
    def __str__(self) -> str:
        return f"\nZooKeeper: {self.name} {self.surname}\nID: {self.ID}\n"+"_"*30