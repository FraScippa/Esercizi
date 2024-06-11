class Specie:
    
    def __init__(self,popolazione_iniziale: int, tasso_crescita: float):
        self.popolazione_iniziale: float = popolazione_iniziale
        self.tasso_crescita: float = tasso_crescita

    def cresci(self) -> float:
        popolazione_nuova: float = self.popolazione_iniziale*(1 + self.tasso_crescita/100)
        self.popolazione_iniziale = popolazione_nuova
        return self.popolazione_iniziale
    
    def getDensita(self, area_kmq: float):
        densita: float = self.popolazione_iniziale/area_kmq
        anni: int = 0
        while densita < 1.0: 
            self.cresci()
            anni += 1
        return anni
                
    def anni_per_superare(self, altra_specie: 'Specie'):
        anni: int = 0
        
        while True:
            self.cresci()
            altra_specie.cresci()
            anni += 1
            if self.popolazione_iniziale < altra_specie.popolazione_iniziale:
                return anni
                
class BufaloKlingon(Specie):
    
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__(popolazione_iniziale, tasso_crescita)

class Elefante(Specie):
    
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__(popolazione_iniziale, tasso_crescita)
    

bufalo_klingon = BufaloKlingon(100, 15)  
elefante = Elefante(10, 35)
print(elefante.cresci())
print(bufalo_klingon.cresci())
anni_densita = bufalo_klingon.getDensita(1500)
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")