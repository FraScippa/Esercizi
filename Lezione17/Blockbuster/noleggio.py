from film import Film
from movie_genere import Azione, Drama, Commedia

class Noleggio:
    def __init__(self, film_list: list[Film], rented_film: dict[int, list[Film]]):
        
        self.film_list: list[Film] = film_list
        self.rented_film: dict[int, list[Film]] = rented_film
        
    def isAvaible(self, film: Film):
        if film.getTitle() in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        else:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return False
    
    def rentAMovie(self, film: Film, clientID: int):
        self.films: list[Film] = []
        if self.isAvaible(film) == True:
            self.film_list.remove(film)
            self.films.append(film)
            self.rented_film[clientID] = self.films
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile nolegiare il film {film.getTitle()}!")
    
    def giveBack(self, film: Film, clientID: int, days: int):
        if self.isAvaible(film) == False:
            self.film_list.append(film)
            self.films.remove(film)
        if 
            
    
    
            