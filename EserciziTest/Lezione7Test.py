#Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista. (modificato)

#For example:

#Test    Result
#print(rotate_left([1, 2, 3, 4, 5], 2))
#[3, 4, 5, 1, 2]

def rotate_left(elements: list[int], k: int) -> list[int]:
    
   lunghezza: int = len(elements)
   newlist: list[int] = []
   
   if k > lunghezza:
       k = k % lunghezza
    
   newlist = elements[k:] + elements[:k]
    
   return newlist

#print(rotate_left([1, 2, 3, 4, 5], 2))

###############################################################################################################################################

#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

#For example:

#Test                                                                                Result
#print(merge_dictionaries({'x': 5}, {'x': -5}))                                     {'x': 0} 

def merge_dictionaries(dict1: dict[str,int], dict2: dict[str,int]) -> dict[str,int]:
    
    for k,v in dict2.items():
        if k in dict1:
            dict1[k] += v
        else:
            dict1[k] = v
    
    return dict1

#print(merge_dictionaries({'x': 5}, {'x': -5}))
#print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

#Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    
    for k,v in da_rimuovere.items():
        for _ in range(v):
            if k in lista:
                lista.remove(k)
    return lista
 
#print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))
#print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
#print(rimuovi_elementi([1, 1, 1, 1], {1: 2}))
#print(rimuovi_elementi([4, 5, 6], {1: 3}))
#print(rimuovi_elementi([], {2: 1}))

######################################################################################################################################################################

#Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, 
#scontati del 10%.

#For example:

#Test    Result
#print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
#{'Zaino': 45.0, 'Quaderno': 19.8}
#print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 
#{}

def filtra_e_mappa(prodotti: dict[str,float]) -> dict[str,float]:
    
    diz1: dict[str,float] = {}
    
    for k,v in prodotti.items():
        if v > 20:
            diz1[k] = v - (v*0.1)
    return diz1

########################################################################################################################################################################

#Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.

#Test                                                                                          Expected                                                                     
#print(remove_elements({1, 2, 3, 4}, [2, 3]))                                                   {1, 4}

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    
    for x in elements_to_remove:
        if x in original_set:
            original_set.remove(x)
    return original_set

#print(remove_elements({1, 2, 3, 4}, [2, 3]))
#print(remove_elements({5, 6, 7}, [7, 8, 9]))
#print(remove_elements({1, 2}, [3]))
#print(remove_elements(set(), [1, 2, 3]))

########################################################################################################################################################################

#Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

#Test    Expected    Got
#print(frequency_dict(['mela', 'banana', 'mela']))
#{'mela': 2, 'banana': 1}
#{'mela': 2, 'banana': 1}

def frequency_dict(elements: list[str]) -> dict[str,int]:
    
    #from collections import Counter
    #diz1: dict[str, int] = dict(Counter(elements))
    #return diz1
    
    diz1: dict[str,int] = {}
    
    for x in elements:
        if x in diz1:
            diz1[x] += 1
        else:
            diz1[x] = 1
        
    return diz1
        
#print(frequency_dict(['mela', 'banana', 'mela']))
#print(frequency_dict([1, 2, 2, 3, 3, 3]))
#print(frequency_dict([]))
#print(frequency_dict(['a', 'b', 'c', 'a', 'b', 'c', 'a']))
#print(frequency_dict([True, False, True]))

class RecipeManager:
    
    def __init__(self):
        self.diz1: dict[str, list[str]] = {}
    
    def create_recipe(self, name: str, ingredients: list[str]) -> dict[str,list[str]]:
        
        if name not in self.diz1:
            self.diz1[name] = ingredients
            return self.diz1
        else:
            return "Errore esiste già"
        
    def add_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name in self.diz1 and ingredient not in self.diz1[recipe_name]:
            self.diz1[recipe_name].append(ingredient)
            return self.diz1
        else:
            return "Errore ricetta non esistente o ingrediente già esistente"
    
    def remove_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name in self.diz1 and ingredient in self.diz1[recipe_name]:
            self.diz1[recipe_name].remove(ingredient)
            return self.diz1
        else:
            return "Ricetta non trovata o ingrediente non trovato"

    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        if recipe_name in self.diz1 and old_ingredient in self.diz1[recipe_name]:
            self.diz1[recipe_name].remove(old_ingredient)
            self.diz1[recipe_name].insert(-1,new_ingredient)
            return self.diz1
        else:
            return "Errore"
        
    def list_recipes(self):
        for k in self.diz1.keys():
            return f"['{k}']"
    
    def list_ingredients(self, recipe_name: str):
        if recipe_name in self.diz1:
            return self.diz1[recipe_name]
        else:
            return "Errore"
    
    def search_recipe_ny_ingredient(self, ingredient: str):
        if ingredient in self.diz1:
            return self.diz1[ingredient]
        else:
            return "Errore"

        
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Mozzarella"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))