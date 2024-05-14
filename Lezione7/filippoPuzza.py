class Animal:
    
    def __init__(self, name:str, species:str, age:int,
                       widht:int, height:int,
                       preferred_habitat:str) -> None:
        self.name: str = name
        self.species: str = species        
        if 100 > age > 0 :
            self.age: int = age
        else:
             raise ValueError("animal age non può essere 0 o >= 100") 
        if widht > 0:
            self.widht: int= widht
        else:
             raise ValueError("animal width non può essere 0") 
        if height > 0:
            self.height: int = height
        else:
             raise ValueError("animal height non può essere 0")               
        self.preferred_habitat: str = preferred_habitat       
        self.health: float = round(100 * (1 / age), 3)
        self.fence = None
        self.fence_area = None


    def area_remaining(self) -> float:       
        single_area_occupation = 0       
        for animal in self.fence:
            single_area_occupation += (animal.widht * animal.height)
        
        area_left =  self.fence_area - single_area_occupation       
        return area_left
    

    def get_name(self) -> str:
        return self.name
    def get_species(self) -> str:
        return self.species
    def get_age(self) -> int:
        return self.age
    def get_widht(self) -> float:
        return self.widht
    def get_height(self) -> float:
        return self.height
    def get_preferred_habitat(self) -> str:
        return self.preferred_habitat
    def get_health(self) -> float:
        return self.health


    def __str__(self) -> str:
        return f"\nAnimal(name={self.get_name()}, species={self.get_species()}, age={self.get_age()}, widht{self.get_widht()}, height={self.get_height()}, preferred_habitat={self.get_preferred_habitat()}, health={self.get_health()})\n"


class Fence:
    
    def __init__(self, area:int, temperature:int, habitat:str) -> None:
        self.area: int = area
        self.temperature: int = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = []
        
    
    def area_remaining(self) -> float:
        single_area_occupation = 0
        for animal in self.animals:
            single_area_occupation += (animal.widht * animal.height)
        
        return self.area - single_area_occupation


    def area_occupated(self) -> float:
        all_animal_occupation = 0
        for animal in self.animals:
            animal_occupation = animal.widht * animal.height
            all_animal_occupation += animal_occupation
        return all_animal_occupation


    def get_area(self) -> int:
        return self.area
    def get_temperature(self) -> int:
        return self.temperature
    def get_habitat(self) -> str:
        return self.habitat
    def get_animals(self) -> list[Animal]:
        return self.animals


    def __str__(self) -> str:
        s: str = f"\nFences:\n\nFence(area={self.get_area()}, temperature={self.get_temperature()}, habitat={self.get_habitat()})\n\nwith animals:\n "
        for animal in self.get_animals():
            s += animal.__str__()
        return s


class ZooKeeper:
    
    def __init__(self, name_k:str, surname:str, id:int) -> None:
        self.name_k = name_k
        self.surname = surname
        self.id = id
    

    def add_animal(self ,animal: Animal ,fence: Fence) -> None:                              
        if animal in fence.animals:
            raise Exception(f"Animal:{animal.name}, is already in the fence")
        else:            
            if animal.preferred_habitat == fence.habitat:
                animal_occupation = animal.height * animal.widht  
                if fence.area_remaining() < animal_occupation:
                    raise Exception(f"Animal:{animal.name}, is too heavy")
                else:                                                                                                                      
                    fence.animals.append(animal)                       
                    animal.fence = fence.animals
                    animal.fence_area = fence.area
            else:
                raise Exception(f"l'habitat:{animal.preferred_habitat} of Animal:{animal.name}, it's not the same with the habitat of the fence:{fence.habitat}")                    


    def remove_animal(self, animal: Animal, fence = Fence) -> None:
        if animal in fence.animals:
            fence.animals.remove(animal)
            animal.fence = None
            animal.fence_area = None            
        elif animal not in fence.animals:
            raise Exception(f"You can't remove {animal.name} beacause he's not part of the fence")               
                   

    def feed_animal(self, animal : Animal) -> None:
        new_animal_occupation: float = 0
        additional_widht = 0
        additional_height = 0                          
        
        if animal in animal.fence:
            additional_widht = animal.widht * 2 / 100
            additional_height = animal.height * 2 / 100
            new_animal_occupation += additional_widht + additional_height 
            
            if animal.area_remaining() >= new_animal_occupation:
                
                if animal.health < 100:
                    animal.health = animal.health + animal.health * 1 / 100
                    animal.widht = animal.widht + animal.widht * 2 / 100
                    animal.height = animal.height + animal.height * 2 / 100                     
                else:
                    raise Exception(f"{animal.name} healt is too high")
            else:
                raise Exception(f"{animal.name}, can't eat beacause he will get too big for the fence")              
        elif animal.fence == None:
            raise Exception(f"You can't feed {animal.name} beacause he's not part of the fence")  

    
    def clean_fence(self, fence: Fence) -> float:                                                                                                
        counter = len(fence.animals)                
        
        if fence.area_remaining() > 0:     
            cleaning_time: float = fence.area_occupated() / fence.area_remaining()
            while counter != 0:
                for animal in fence.animals:                    
                    counter -= 1
                    animal.fence = None
                    animal.fence_area = None                                 
                fence.animals.clear()
                return cleaning_time
        else:
            while counter != 0:
                for animal in fence.animals:                    
                    counter -= 1
                    animal.fence = None
                    animal.fence_area = None                                 
                fence.animals.clear()            
            return fence.area
    

    def get_name_k(self) -> str:
        return self.name_k
    def get_surname(self) -> str:
        return self.surname
    def get_id(self) -> int:
        return self.id
    
    def __str__(self) -> str:
        s: str = f"Guardians:\nZooKeeper(name={self.get_name_k()}, surname={self.get_surname()}, id={self.get_id()})\n\n"
        return s

class Zoo:

    def __init__(self, fence : list[Fence], zookeeper : list[ZooKeeper]) -> None:       
        self.fence: list[Fence] = fence
        self.zookeeper: list[ZooKeeper]= zookeeper


    def describe_zoo(self):
        s: str = "Guardians:\n\n"
        
        for zookeeper in self.zookeeper:
            s += f"ZooKeeper(name={zookeeper.get_name_k()}, surname={zookeeper.get_surname()}, id={zookeeper.get_id()})\n"        
        
        for fence in self.fence:
            if fence.get_animals():  
                s += "#" * 30 +f"\nFences:\n\nFence(area={fence.get_area()}, temperature={fence.get_temperature()}, habitat={fence.get_habitat()})\n\nWith animals:\n\n"
                for animal in fence.get_animals():
                    s += f"Animal(name={animal.get_name()}, species={animal.get_species()}, age={animal.get_age()}, widht{animal.get_widht()}, height={animal.get_height()}, preferred_habitat={animal.get_preferred_habitat()}, health={animal.get_health()})\n"
        return s  

    
    

fence1 = Fence(100, 20, "Continent")
fence2 = Fence(2000, 20, "Continent")
animal1 = Animal("Scoiattolo", "Blabla", 25, 2, 50, "Continent")
animal2 = Animal("Lupo", "Lupus", 10, 1, 900, "Continent")
animal3 = Animal("lalal", "laalla", 20, 1, 2, "Continent")
animal4 = Animal("4", "Blabla", 25, 2, 5, "Continent")
animal5 = Animal("5", "Lupus", 10, 20, 12, "Continent")
animal6 = Animal("6", "laalla", 20, 1, 2, "Continent")
guardiano1 = ZooKeeper("Mario","Rossi",12345)
guardiano2 = ZooKeeper("Mario","Rossi",12345)
zoo1 = Zoo(fence = [fence1,fence2], zookeeper=[guardiano1,guardiano2])


#guardiano1.feed_animal(animal4) #se non inserito in un fence da errore

print(zoo1.describe_zoo())