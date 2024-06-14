class Persona:

    def __init__(self, first_name: str, last_name: str, age:int = 0):
        self.setName(first_name)
        self.setLastName(last_name)
        self.setAge(age)
        
        if type(self.__first_name) == str and type(self.__last_name) == str:
            self.setAge(0)
    
    def setName(self, first_name: str):
        self.__first_name: str = first_name
        
        if type(self.__first_name) == str:
            return self.__first_name
        else:
            self.__first_name = None
            return "Il nome inserito non è una stringa!"
    
    def setLastName(self, last_name: str):
        self.__last_name: str = last_name
        if type(self.__last_name) == str:
            return self.__last_name
        else:
            self.__last_name = None
            return "Il cognome inserito non è una stringa!"

    def setAge(self, age: int):
        self.__age: int = age
        if self.__age >= 0:
            return self.__age
        else:
            self.__age = None
            print("L'età deve essere un numero intero!")

    def getName(self):
        return self.__first_name
    
    def getLastname(self):
        return self.__last_name
    
    def getAge(self):
        return self.__age
    
    def greet(self):
        print(f"Ciao, sono {self.getName()} {self.getLastname()}! Ho {self.getAge()} anni!")

