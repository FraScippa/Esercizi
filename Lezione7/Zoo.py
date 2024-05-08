#Francesca Scippa

#08-05-2024

#senza test!

class Animal:

    def __init__(self, name: str, species: str, age: int):

        self.name: str = name
        self.species: str = species
        self.age: int = age
    
    def __str__(self) -> str:
        return f"Animal's name: {self.name}\nSpecies: {self.species}\nAge: {self.age}"

class Fance:
    
    def __init__(self, dimensions: float, temperature: float, habitat: str, animals: list[Animal] = []):

        self.dimensions: float = dimensions
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = animals
    
    def __str__(self):
        return f"Dimensions: {self.dimensions}\nTemperature: {self.temperature}\nAnimals: {self.animals}"

class ZooKeeper:

    def __init__(self, name: str, surname: str, ID: int):
        
        self.name: str = name
        self.surname: str = surname
        self.ID: int = ID
    
    def add_animal(self, animals: Animal, fance: Fance):
        self.fance.append(animals)

    def remove_animal(self, animal: Animal):
        self.animals.remove(animal)
    
    def __str__(self) -> str:
        return f"ZooKeeper: {self.name} {self.surname}\nID: {self.ID}"
    
    #health: int = 0

    #def feed(self, animal: Animal):
        #health += 1
        #height-wheight +2%
        #healt += 1

    def clean(self, fance : Fance) -> float: #Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto.
        if fance in self.fance:
            self.fance: int = 0
        
class Zoo:
    
    def __init__(self, fance: list[Fance], animals: list[Animal], guardians: list[ZooKeeper]):
        
        self.fance: list[Fance] = fance
        self.animals: list[Animal] = animals
        self.guardians: list[ZooKeeper] = guardians
    
    def __str__(self):
        return f"Fances: {self.fance}\nAnimals: {self.animals}\nGuardians: {self.guardians}"
        
   # def describe_zoo(self):
       # return __str__()


zebra: Animal = Animal("Giggino", "Zebra", 15)
leone: Animal = Animal ("Paolo", "Leone", 20)

print(zebra)
print(leone)

zookeeper: ZooKeeper = ZooKeeper("Ferdinando", "Paolini", 5457)
zookeeper1: ZooKeeper = ZooKeeper("Nicolò", "Di Silvestro", 7080)

print(zookeeper,"\n",zookeeper1)

animal: Fance = Fance(100, -10, "Artic" )

animal.add_animal(zebra)

print(animal)









