from abc import ABC, abstractmethod
import string

class CodificatoreMessaggio(ABC):
    
    @abstractmethod
    def codifica_signolo(self, car: str):
        #import string
        #alfabeto: str = string.ascii_lowercase 
        alfabeto: list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
        if car.lower() in alfabeto:
            index = alfabeto.index(car.lower())
            return index 
    
    @abstractmethod
    def codifica(self, mess_codificare: str)-> int:
        s = ''
        for c in mess_codificare:
            mess = str(self.codifica_signolo(c))
            s += f' {mess}'
        return s

class DecodificatoreMessaggio(ABC):
    
    def decodifica(self, testo_codificato: str):
        alfabeto: list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for c in testo_codificato:
            mess = testo_codificato.strip()
        
        return alfabeto[mess]
            
        
        
        
    
class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    
    def __init__(self, chiave: int):
        self.chiave: int = chiave
    
    def sposta_carattere(self, car: str):
        alfabeto: str = string.ascii_lowercase + string.ascii_uppercase
        for i in alfabeto:
            if car in alfabeto:
                return i
            
            
print()