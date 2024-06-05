#Francesca Scippa
#02-06-2024

#Sistema di Gestione Biblioteca#

class Libro:
    
    def __init__(self, title: str, autore: str, prestato: bool = False):
        
        self.title: str = title
        self.autore: str = autore
        self.prestato: bool =  prestato
    
    def __str__(self):
        return f"\tTitolo: {self.title} | Autore: {self.autore} | Prestato: {self.prestato}\n"

class Biblioteca:
    
    def __init__(self):
        self.biblioteca: list[Libro] = []
    
    def aggiungi_libro(self, libro: Libro):
        if libro not in self.biblioteca:
            self.biblioteca.append(libro)
    
    def presta_libro(self, titolo: str):
        for l in self.biblioteca:
            if titolo == l.title:
                l.prestato = True
                return "La richiesta di prestito è andata a buon fine!" 
        return 'Il libro è già stato dato in prestito'
    
    def restituisci_libro(self, titolo: str):
        for l in self.biblioteca:
            if titolo == l.title and l.prestato == True:
                l.prestato = False
                return "Il libro è stato restituito con successo! Grazie."
        return "Il libro non è stato prestato" 
    
    def __str__(self) -> str:
        s: str = ''
        for x in self.biblioteca:
            s += f'\t{x}\n'
        return s
        
    def mostra_libri_disponibili(self):
        if len(self.biblioteca) > 0:
            print(self.__str__())
        else:
            print('Errore: non ci sono libri.')

#Catalogo Film#

class Regista:
    
    def __init__(self, nome: str, films: list[str] = []):
        self.nome: str = nome
        self.films: list[str] = films

    def __str__(self):
        return f"\n\tRegista: {self.nome} | Films: {self.films}"

class CatalogoFilm:
    
    def __init__(self):
        self.catalogo: list[Regista] = []

    def aggiungi_film(self, regista: Regista, film: str):
        for r in self.catalogo:
            if r.nome == regista.nome:
                if film not in r.films:
                    r.films.append(film)
                    return f"## lista di {regista} aggiornata con successo! ##"
                else:
                    return f'## Il film {film} è già presente nella lista di {regista.nome} ##'
        regista.films.append(film)
        self.catalogo.append(regista)
        return f'Regista: {regista.nome} aggiunto con i film {regista.films}'
    
    def remove_film(self, regista: str, film: str):
        for r in self.catalogo:
            if regista == r.nome:
                if film in r.films:
                    r.films.remove(film)
                    if len(r.films) == 0:
                        self.catalogo.remove(r)
                        return f"## Dato che la lista di questo regista è vuota è stato elimiato ##"
                    return f'## Il film, {film}, è stato rimosso con successo! ##'
                return '## Non ci sono film di questo regista ##' 
        return "## Il regista non è presente nel catalogo ##"
    
    def __str__(self) -> str:
        s: str = ''
        for x in self.catalogo:
            s += f'{x} '
        return s 
    
    def lista_registi(self):
        print(self.__str__())
    
    def get_film_regista(self, regista: str):
        for r in self.catalogo:
            if regista == r.nome:
                return f"{regista} films: {r.films}"
        return '## Il regista non è presente nel catalogo ##'
    
    def cerca_titolo_film(self, titolo: str):
        results: list[str] = []
        for r in self.catalogo:
            for f in r.films:
                if titolo.lower() in f.lower():
                    results.append((f"{r.nome}: {f}"))
        if results:
            return results
        else:
            return '### Errore: inserire un altra parola ###'
       