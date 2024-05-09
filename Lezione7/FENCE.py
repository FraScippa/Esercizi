from ANIMALS import Animal

class Fence:
    
    savana: list = []
    aritc: list = []
    ocean: list = []
    
    def __init__(self, area: float, temperature: float, 
                 habitat: str,  animals = None):
        
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[str] = []
        
        
        if animals is None:
            pass
        else:
            self.add_animals(animals)
    
    def add_animals(self, animals: list[Animal]):
        for animal in self.animals:
            self.animals.append(animal.species)
            
    def __str__(self):
        return f"Area: {self.area}\nTemperature: {self.temperature}\nHabitat: {self.habitat}\nAnimals: {self.animals}"
