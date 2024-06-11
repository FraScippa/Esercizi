#Francesca Scippa
#07-06-2024

class Media:
    
    def __init__(self):
        self.title = None
        self.reviews: list[int] = []
        
    def set_title(self, title: str):
        self.title = title

    def get_title(self):
        return self.title
    
    def aggiungiValutazine(self, voto: int):
        if voto <= 5:
            self.reviews.append(voto)
    
    def getMedia(self) -> float:
        media: float = round(sum(self.reviews)/len(self.reviews),2)
        return media
    
    def getRate(self) -> str:
        media: float = self.getMedia()
        s : str = ""
        if 0 <= media <= 1.5:
            s = "Terribile"
        if 1.6 < media <= 2:
            s = "Brutto"
        if 2.6 < media <= 3:
            s ="Normale"
        if 3.6 < media <= 4:
            s ="Bello"
        if 4.6 < media <= 5:
            s = "Grandioso"
        return s
          
    def ratePercentage(self, voto: int):
        v: float = self.reviews.count(voto)
        perc: float = round((v/len(self.reviews))*100,2)
        return f"{perc}%"
    
    def recensione(self):
        s: str = ''
        s += f"Titolo del Film: {self.get_title()}\nVoto Medio: {self.getMedia()}\nGiudizio: {self.getRate()}"
        s += f"\nTerribile: {self.ratePercentage(1)}\nBrutto: {self.ratePercentage(2)}"
        s += f"\nNormale: {self.ratePercentage(3)}\nBello: {self.ratePercentage(4)}"
        s += f"\nGrandiodo: {self.ratePercentage(5)}"
        return s


class Film(Media):
    def __init__(self, title: str):
        super().__init__()
        self.set_title(title)

###########################################################################################################

class Contatore:
    def __init__(self, conteggio: int = 0):
        self.conteggio = conteggio
    
    def setZero(self):
        self.conteggio = 0
        return self.conteggio

    def add1(self):
        self.conteggio += 1
        return self.conteggio
    
    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -= 1
        elif self.conteggio <= 0:
            print("Non è possibile eseguire la sottrazione")
        
    def get(self):
        return self.conteggio
    
    def mostra(self):
        s: str = ''
        s += f"Conteggio attuale: {self.conteggio}"
        print(s) 

##################################################################################################################	

class RecipeManager:
    def __init__(self):
        self.recipe: dict[str,list[str]] = {}
        self.ingredients: list[str] = []
    
    def create_recipe(self, name: str, ingredients: list[str] = []):
        if name not in self.recipe.keys():
            self.recipe[name] = ingredients
            for x in ingredients:
                self.ingredients.append(x)
            return self.recipe
        else:
            print("Errore")
    
    def add_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name in self.recipe.keys():
            if ingredient not in self.recipe[recipe_name]:
                self.ingredients.append(ingredient)
                return f"{{'{recipe_name}': {self.ingredients}}}"
        else:
            print("Errore")

    def remove_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name in self.recipe.keys():
            self.ingredients.remove(ingredient)
            return f"{{'{recipe_name}': {self.ingredients}}}"
        else:
            print("Errore")

    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        if recipe_name in self.recipe.keys():
            if old_ingredient in self.recipe[recipe_name]:
                self.ingredients.remove(old_ingredient)
                self.ingredients.insert(-1,new_ingredient)
                return f"{{'{recipe_name}': {self.ingredients}}}"
        else:
            print("Errore ingr. no esistente")
        
    def list_recipes(self):
        for x in self.recipe.keys():
            return [x]

    def list_ingredients(self, recipe_name: str):
        if recipe_name in self.recipe.keys():
            for _ in self.recipe.items():
                return self.ingredients
        return f"{recipe_name} non esiste."
    
    def search_recipe_by_ingredient(self, ingredient: str):
        for k, v in self.recipe.items():
            if ingredient in v:
                return f"{{'{k}': {self.ingredients}}}"             
        
##############################################################################################################

class Veicolo:
    
    def __init__(self, marca: str, modello: str, anno: int):
        
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno
    
    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}')
    
class Auto(Veicolo):
    
    def __init__(self, marca:str, modello: str, anno: int, numero_porte: int):
        super().__init__(marca, modello, anno)
        self.numero_porte: int = numero_porte
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")
        

class Moto(Veicolo):
    
    def __init__(self, marca: str, modello: str, anno: int, tipo: str):
        super().__init__(marca, modello, anno)
        self.tipo: str = tipo
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")

###################################################################################################################

class Specie:
    
    def __init__(self,popolazione_iniziale: int, tasso_crescita: float):
        self.popolazione_iniziale: float = popolazione_iniziale
        self.tasso_crescita: float = tasso_crescita

    def cresci(self) -> float:
        self.popolazione_iniziale*=(1 + self.tasso_crescita/100)
        return self.popolazione_iniziale
    
    def getDensita(self, area_kmq: float) -> int:
        densita: float = self.popolazione_iniziale/area_kmq
        anni: int = 0
        while densita < 1:
            anni += 1
            self.cresci()
            densita: float = self.popolazione_iniziale/area_kmq
        
        return anni 
                
    def anni_per_superare(self, altra_specie: 'Specie'):
        anni: int = 0
        
        while anni < 1000:
            self.cresci()
            altra_specie.cresci()
            anni += 1
            if self.popolazione_iniziale > altra_specie.popolazione_iniziale:
                return anni
                
class BufaloKlingon(Specie):
    
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__(popolazione_iniziale, tasso_crescita)

class Elefante(Specie):
    
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__(popolazione_iniziale, tasso_crescita)
    
##################################################################################################################          
     
