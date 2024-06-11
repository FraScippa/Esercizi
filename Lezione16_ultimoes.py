class Specie:
    
    def __init__(self,popolazione_iniziale: int, tasso_crescita: float):
        self.popolazione_iniziale: int = popolazione_iniziale
        self.tasso_crescita: float = tasso_crescita
    
    def set_nome(self, nome: str):
        self.nome = nome
        return self.nome

    
    def cresci(self) -> float:
        popolazione_nuova: float = self.popolazione_iniziale*(1 + self.tasso_crescita/100)
        return popolazione_nuova
    
    def getDensita(self, area_kmq: float):
        densita: float = self.popolazione_iniziale/area_kmq
        
        while densita <= 1: 
            self.cresci()
                
            
    def anni_per_superare(self, altra_specie: 'Specie'):
        anni: int = 0
        
        while anni < 1000:
            if self.popolazione_iniziale < altra_specie.popolazione_iniziale:
                self.cresci()
                altra_specie.cresci()
                anni += 1
        
        return anni
       
class BufaloKlingon(Specie):
    
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__(popolazione_iniziale, tasso_crescita)

class Elefante(Specie):
    
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__(popolazione_iniziale, tasso_crescita)
    

bufalo_klingon = BufaloKlingon(100, 15)  
elefante = Elefante(10, 35)

anni_necessari = elefante.anni_per_superare(bufalo_klingon)  
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")