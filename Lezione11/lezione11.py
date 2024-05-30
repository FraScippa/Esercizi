class Film:

    def __init__(self, titolo: str, durata: float):

        self.titolo: str = titolo
        self.durata: float = durata


    def __str__(self) -> str:
        return f"Il film che hai scelto è: {self.titolo} e dura: {self.durata}"


class Sala:

    def __init__(self, n_sala: int, titolo: str, posti_tot: int, posti_occ: int):
        
        
        self.n_sala: int = n_sala
        self.titolo: str = titolo
        self.posti_tot: int = posti_tot
        self.posti_occ: int = posti_occ
        self.posti_rimanenti: int = posti_tot - posti_occ
        
    def prenota_posti(self, num_posti: int):
        
        if self.posti_rimanenti >= num_posti:
            self.posti_rimanenti -= num_posti
        else:
            print("Non ci sono abbastanza posti per questo film!")
        
    def posti_disponibili(self):
        posti_disponibil: int = self.posti_tot - self.posti_occ
        return f"i posti disponibili sono: {posti_disponibil}"

    def __str__(self) -> str:
        return f'Sala: {self.n_sala}, titolo: {self.titolo}, posti totali: {self.posti_rimanenti}'
class Cinema:

    def __init__(self):
        self.sale: list[Sala] = []


    def aggiungi_sala(self, sala: Sala):
        if sala not in self.sale:
            self.sale.append(sala)
    
    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        for _ in self.sale:
                if titolo_film in self.sale and num_posti <= Sala.posti_rimanenti:
                    return f"Il tuo posto è stato prenotato con successo!"
                else:
                    return f"Purtropo questo film non ha più posti disponibili."
    
    def __str__(self) -> str:
        s: str = ''
        for x in self.sale:
            s += f' le sale sono: {x}'
        return s
        
cinema_1: Cinema = Cinema()
film_1: Film = Film('Ocean Twelve', 1.49)
film_2: Film = Film('Ciao', 1.46)
sala_1: Sala = Sala(4, 'Ocean Twelve', 1790, 11)
sala_2: Sala = Sala(7, 'Ciao', 1701, 100)

sala_1.prenota_posti(5)

print(sala_1.posti_disponibili())

cinema_1.aggiungi_sala(sala_1)
cinema_1.aggiungi_sala(sala_2)

print(cinema_1)





        
    

    