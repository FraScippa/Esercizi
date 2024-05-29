from abc import ABC, abstractmethod #per dichiarare una classe astratta

class AbcAnimal(ABC): #abstract class, classe astratta

    @abstractmethod
    def verso(self) -> str: #tutte le classi dovranno riscrivere questa funzione se ereditano questa classe.
        pass


class Cane(AbcAnimal): #tipo di dato personalizzato (in questo caso è di tipo Cane). Eredita la classe astratta, quindi dovrà riscrivere la funzione 'verso'

    def __init__(self, nome:str) -> None:
        self.nome: str = nome

    def verso(self) -> str:
        print('Bay')
        return ''

class Cat(AbcAnimal): #tipo di dato personalizzato (in questo caso è di tipo Gatto)

    def __init__(self, nome:str) -> None:
        self.nome: str = nome

    def verso(self) -> str:
        print('Miao!')
        return ''

class Coccodrillo(AbcAnimal): #tipo di dato personalizzato (in questo caso è di tipo Coccodrillo)

    def __init__(self, nome:str) -> None:
        self.nome: str = nome
#se non implementiamo la funzione della classe astratta, ci darà errore. Dobbiamo sempre sovrascrivelo!

    def verso(self) -> str:
        print('Bho')
        return ''


from typing import Any #Any: indica qualsiasi cosa, sto importando la classe Any.Any sta sopra a tutto, prende qualsiasi cosa. (tenta di evitare)

from typing import TypeAlias
tipocomppsto: TypeAlias = dict[int, Any] #puoi anche utilizzare Any all'interno di TypeAlias.


a: dict[str, tipocomppsto] = {    #dict[str, Any]     |:or logico per dire che possono essere uno dei due tipi (str | int). Con la typizzazione già so cosa dovrò aspettarmi dalle variabili.
    'key_1':{1:''},
    'key_2':{2:''},
    'key_3':{3:''}
    }
    

cane1: Cane = Cane(nome = 'Pluto')
gatto1: Cat = Cat(nome = 'SIlvestro')
coccodrillo1: Coccodrillo = Coccodrillo (nome = 'Giovanni')

lista_animali: list[AbcAnimal] = [cane1, gatto1, coccodrillo1]

for animale in lista_animali:

    animale.verso()

#cane1.verso()
#gatto1.verso()
#coccodrillo1.verso()