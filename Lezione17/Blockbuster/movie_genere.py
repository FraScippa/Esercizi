
from film import Film

class Azione(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.__genere: str = "Azione"
        self.__penale: float = 3.00
    
    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, days: float):
        return self.getPenale()*days
    
class Commedia(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.__genere: str = "Commedia"
        self.__penale: float = 2.50

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, days: float):
        return self.getPenale()*days
    
class Drama(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.__genere: str = "Drama"
        self.__penale: float = 2.00

    def getGenere(self):
        return self.__genere
    
    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, days: float):
        return self.getPenale()*days