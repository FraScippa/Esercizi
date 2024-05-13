from ANIMALS import Animal

class Fence:
    
    def __init__(self, area: float, temperature: float, 
                 habitat: str,  animals: list[Animal] = None, animal: Animal = 0):
        
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[str] = []
        
        if animals is None:
            pass
        else:
           animals.append(animal)
    
    def get_area(self):
        return self.area  
    
    def __str__(self):
        return '#'*30+f"\nEmpty Area: {self.area}\nTemperature: {self.temperature}\nHabitat: {self.habitat}\nAnimals: {self.animals}\n"+ '#'*30
       