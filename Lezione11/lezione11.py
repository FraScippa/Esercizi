#Francesca Scippa
#30-05-2024

#SISTEMA DI PRENOTAZIONE CINEMA#

class Film:

    def __init__(self, titolo: str, durata: float):

        self.titolo: str = titolo
        self.durata: float = durata
        

    def __str__(self) -> str:
        return f"{self.titolo} e dura: {self.durata}"


class Sala:

    def __init__(self, n_sala: int, film: Film, posti_tot: int, posti_occ: int):
        
        
        self.n_sala: int = n_sala
        self.film: Film = film
        self.posti_tot: int = posti_tot
        self.posti_occ: int = posti_occ
        self.posti_rimanenti: int = posti_tot - posti_occ
    
    def get_posti_rimanenti(self):
        return self.posti_rimanenti
    
    def prenota_posti(self, num_posti: int):
        if self.posti_rimanenti >= num_posti:
            self.posti_rimanenti -= num_posti
        else:
            print("Non ci sono abbastanza posti per questo film!")
        
    def posti_disponibili(self):
        posti_disponibil: int = self.posti_tot - self.posti_occ
        return f"i posti disponibili sono: {posti_disponibil}"

    def __str__(self) -> str:
        return f'Sala: {self.n_sala}, titolo: {self.film}, posti totali: {self.posti_rimanenti}'
class Cinema:

    def __init__(self):
        self.sale: list[Sala] = []


    def aggiungi_sala(self, sala: Sala):
        if sala not in self.sale:
            self.sale.append(sala)
    
    def prenota_film(self, titolo_film: str, num_posti: int):
        for sala in self.sale:
                if titolo_film == sala.film.titolo:
                    if num_posti <= sala.get_posti_rimanenti():
                        sala.prenota_posti(num_posti)
                        return f"Il tuo posto per {titolo_film}. è stato prenotato con successo!"
                    else:
                        return f'Non ci sono abbastanza posti liberi per questo film: {titolo_film}'
        return "Film Non Presente"       
    
    def __str__(self) -> str:
        s: str = ''
        for x in self.sale:
            s += f'{x} '
        return s
    


#GESTIONE DI UN MAGAZZINO#


class Prodotto:
    def __init__(self, nome: str, quantita: int):
        self.nome: str = nome
        self.quantita: int = quantita

    def __str__(self) -> str:
        return f"Prodotto: {self.nome} | Quantità: {self.quantita}"

class Magazzino:

    def __init__(self):
        self.magazzino: list[Prodotto] = []

    def aggiungi_prodotto(self, new_prodotto: Prodotto):
        if new_prodotto not in self.magazzino:
            self.magazzino.append(new_prodotto)
    
    def cerca_prodotto(self, nome: str) -> Prodotto:
        for prod in self.magazzino:
            if nome == prod.nome:
                return prod
        return "Il prodotto richiesto è inesistente."
    
    def verifica_disponibilità(self, nome: str) -> str:
        for p in self.magazzino:
            if nome in p.nome and p.quantita > 0:
                return "Il prodotto che stai cercando è disponibile"
        return "Il prodotto non è disponibile"
    
    def __str__(self) -> str:
        s: str = ''
        for x in self.magazzino:
            s += f'\n{x}\n'
        return s
        
    