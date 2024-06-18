from film import Film
from movie_genere import Azione, Commedia, Drama

class Noleggio:
    def __init__(self, film_list: list[Film], rented_film: dict[int, list[Film]]):
        
        self.film_list: list[Film] = film_list
        self.rented_film: dict[int, list[Film]] = {}
        
    def isAvailable(self, film: Film):
        for movie in self.film_list:
            if film.isEqual(movie):
                print(f"Il film scelto è disponibile: {film.getTitle()}!")
                return True
        print(f"Il film scelto non è disponibile: {film.getTitle()}!")
        return False
    
    def rentAMovie(self, film: Film, clientID: int):
        self.films: list[Film] = []
        if self.isAvaible(film) == True: #????
            self.film_list.remove(film)
            self.films.append(film)
            self.rented_film[clientID] = self.films
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile nolegiare il film {film.getTitle()}!")
    
    def giveBack(self, film: Film, clientID: int, days: int):
        if clientID in self.rented_film and film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            self.film_list.append(film)
            penale = film.calcolaPenaleRitardo(days) #?!?!?!?!?
            print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} è di {penale} euro!")
        else:
            print(f"Il cliente {clientID} non ha noleggiato il film {film.getTitle()}!")
    

    def printMovies(self):
        for film in self.film_list:
            print(f"{film.getTitle()}-{genere}-")#?!?!?!?!?
    
    def printRentMovies(self, clientID: int):
        if clientID in self.rented_film.keys():
            print(f"{self.rented_film[clientID]}")



        
    
    
            