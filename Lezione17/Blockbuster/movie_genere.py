
from film import Film

class Azione(Film):
    def __init__(self, genere: str, penale: float, id: int, title: str):
        super().__init__(id, title)
        self.genere: str = "Azione"
        self.penale: float = 3.00
    
    def getGenere(self):
        return self.genere
    
    def getPenale(self):
        return self.penale
    
    def calcolaPenaleRitardo(self, ritardo: float):
        penale: float = self.penale*ritardo
        return penale
    
class Commedia(Film):
    def __init__(self, genere: str, penale: float, id: int, title: str):
        super().__init__(id, title)
        self.genere: str = "Commedia"
        self.penale: float = 2.50

    def getGenere(self):
        return self.genere
    
    def getPenale(self):
        return self.penale
    
    def calcolaPenaleRitardo(self, ritardo: float):
        penale: float = self.penale*ritardo
        return penale
    
class Drama(Film):
    def __init__(self, genere: str, penale: float, id: int, title: str):
        super().__init__(id, title)
        self.genere: str = "Drama"
        self.penale: float = 2.00

    def getGenere(self):
        return self.genere
    
    def getPenale(self):
        return self.penale
    
    def calcolaPenaleRitardo(self, ritardo: float):
        penale: float = self.penale*ritardo
        return penale