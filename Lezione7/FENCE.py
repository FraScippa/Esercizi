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
        animal_info = ''
        for animal in self.animals:
            animal_info += f"{animal.name} ({animal.species}) - Health: {animal.health}\n"
        if not animal_info:
            animal_info = 'Empty fence\n'
        
        return f"{'#'*30}\nEmpty Area: {self.area}\nTemperature: {self.temperature}\nHabitat: {self.habitat}\nAnimals:\n{animal_info}{'#'*30}"
        
       