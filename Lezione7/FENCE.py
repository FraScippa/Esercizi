from ANIMALS import Animal

class Fence:
    
    def __init__(self, area: float, temperature: float, 
                 habitat: str,  animals: list[Animal] = None):
        
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[str] = []
        
        if animals is None:
            pass
        else:
           animals.append(animals)
        
    def __str__(self):
        return '#'*30+f"\nArea: {self.area}\nTemperature: {self.temperature}\nHabitat: {self.habitat}\nAnimals: {self.animals}\n"+ '#'*30
       