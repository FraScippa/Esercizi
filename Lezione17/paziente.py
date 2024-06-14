from persona import Persona

class Paziente(Persona):

    def __init__(self, codice_identificativo: str, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
    
        self.__codice_identificativo: str = codice_identificativo

    def setIdCode(self, idCode: str):
        self.__codice_identificativo = idCode
        return self.__codice_identificativo
    
    def getIdCode(self):
        return self.__codice_identificativo
    
    def patientInfo(self):
        print(f"Paziente: {self.getName()} {self.getLastname()}\nID: {self.getIdCode()}")
