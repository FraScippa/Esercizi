from abc import abstractmethod,abstractclassmethod, ABC

class Forma(ABC):
    def __init__(self, nome: str):
        self.nome: str = nome

    @abstractmethod
    def getArea(self) -> float:
        pass

    def render(self) -> None:
        pass

class Quadrato(Forma):

    def __init__(self, lato: float, nome: str = 'Quadrato'):
        super().__init__(nome)
        self.lato: float = lato
    
    def getArea(self) -> float:
        area: float = self.lato**2
        return area

    def render(self):
        for _ in range(self.lato):
            print("*", end = "")
    
quad: Quadrato  = Quadrato(4)

quad.getArea()
quad.render()

