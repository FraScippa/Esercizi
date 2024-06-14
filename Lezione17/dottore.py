from persona import Persona

class Dottore(Persona):

    def __init__(self, specialization: str, parcel: float, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        
        if type(specialization) == str:
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione non è una stringa")

        if type(parcel) == float:
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcella inserita non è un float!")
    
    def setSpecialization(self, specialization: str):
        self.__specialization: str = specialization
        if type(self.__specialization) == str:
            self.setSpecialization(specialization)
        else:
            print("La speicializzazione inserita non è una stringa!")
    
    def setParcel(self, parcel: float):
        self.__parcel: float = parcel
        if parcel > 0.0:
            self.setParcel(parcel)
        else:
            print("La parcella inserita non è un float!")
        
    def getSpecialization(self):
        return self.__specialization
    
    def getParcel(self):
        return self.__parcel
    
    def isAValidDoctor(self):
        if self.getAge() >= 30:
            print(f"Doctor {self.getName()} {self.getLastname()} is valid!")
            return True
        else:
            print(f"Doctor {self.getName()} {self.getLastname()} is not valid!")
            return False
    
    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.getSpecialization()}")
