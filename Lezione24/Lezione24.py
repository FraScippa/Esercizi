from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):
    
    @abstractmethod
    def codifica(self, mess_codificare: str)-> str:
        pass

class DecodificatoreMessaggio(ABC):
    
    def decodifica(self, testo_codificato: list[int]) -> str:
        alfabeto: list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        dec: str = ''
        for c in testo_codificato:
            dec += alfabeto[c]
        return dec
            
class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    
    def __init__(self, chiave: int):
        self.chiave: int = chiave
    
    def __sposta_carattere(self, car: str): 
        #import string
        #alfabeto: str = string.ascii_lowercase 
        alfabeto: list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        if car.lower() in alfabeto:
            index = alfabeto.index(car.lower())
            return alfabeto[index + self.chiave]
        else:
            return car.lower()
        
    def codifica(self, mess_codificare: str) -> str:
        s = ''
        for c in mess_codificare:
            mess = str(self.__sposta_carattere(c))
            s += f' {mess}'
        return s
            
    