class Animal:

    def __init__(self, name: str, species: str,
                 age: int, height: int, 
                 width: int, preferred_habitat: str, 
                 health:float = None, dimention: int = 0):

        self.animals: list[str] = []
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health: int = round(100*(1/age),3)
        self.dimention: int = width*height

    def get_dimention(self):
        return self.dimention
    
    def __str__(self) -> str:
        return f"Animal's name: {self.name}\nSpecies: {self.species}\nAge: {self.age}\nHeight: {self.height}\nWidth: {self.width}\nHabitat: {self.preferred_habitat}\nHealth: {self.healt}\nDimention: {self.dimention}"
    
    def animal_name(self) -> str:
        return self.name
        