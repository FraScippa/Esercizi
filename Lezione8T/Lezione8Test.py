#Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
#La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione 
#e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e 
#gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.

def rotate_left(elements: list, k: int) -> list:
    # cancella pass e scrivi il tuo codice
    lunghezza: int = len(elements)
    newlist = []
    if k > lunghezza:
        k = k % lunghezza
        
    newlist = elements[k:] + elements[:k]
    
    return newlist

#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, 
#somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # cancella pass e scrivi il tuo codice
    
    dict3 = dict1
   
    for key, value in dict2.items():  
        if key in dict3:
            dict3[key] += value
        else:
            dict3[key] = value
            
    return dict3

#print(merge_dictionaries({'x': 5}, {'x': -5}))

#Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
#Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    # cancella pass e scrivi il tuo codice

    new_lista: lista = lista.copy()
    
    for key, value in da_rimuovere.items():
        for i in range(value):
            if key in new_lista:
                new_lista.remove(key)

    return new_lista

#print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2})) 1,3,4
#print(rimuovi_elementi([], {2: 1}))
#print(rimuovi_elementi([1, 1, 1, 1], {1: 2}))


#Scrivi una funzione che prenda in input una lista di dizionari che rappresentano 
#voti di studenti e aggrega i voti per studente in un nuovo dizionario.

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codice

    diz: dict = {}
    
    for voto in voti:
        nome = voto['nome']
        voto_studente = voto['voto']
        
        if nome in diz:
            diz[nome].append(voto_studente)
        else:
            diz[nome] = [voto_studente]
    
    return diz

#print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))


#PARTE 1
#Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, 
#e-mail (facoltativo) e numero di telefono (facoltativo). 
#La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
#PARTE 2
#Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, 
#il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. 
#Questa funzione dovrebbe aggiornare il dizionario del contatto.

def create_contact(name_surname: str, email: str=None, telefono: int=None) -> dict:
    # cancella pass e scrivi il tuo codice
    
   contact: dict =  {'profile': name_surname, 'email': email, 'telefono': telefono}

   return contact

def update_contact(contact: dict, name: str, email: str =None, telefono: int=None) -> dict:
    # cancella pass e scrivi il tuo codice

    new_contact: dict = {}

    if contact['profile'] != name:
        new_contact['profile'] = name
    else:
        new_contact['profile'] = contact['profile']
        
    if contact['email'] != None:
        new_contact['email'] = contact['email']
    else:
        new_contact['email'] = email

    if contact['telefono'] != telefono:
        new_contact['telefono'] = telefono
    else:
        new_contact['telefono'] = contact['telefono']

    return new_contact

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
#print(update_contact(contact, "Mario Rossi", telefono=123456789))

def update_contact1(contact: dict, name: str, email: str =None, telefono: int=None) -> dict:
    # cancella pass e scrivi il tuo codice

    if contact['profile'] == name:
        
        if email:
           contact['email'] = email
        
        if telefono: #ritorna un boolean, se il telfono è presente sarà True se no False
            contact['telefono'] = telefono
        
    return contact


print(update_contact1(contact, "Laura Neri", email="laura.new@domain.com", telefono=84736736))
        
#Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca 
#un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.

def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    # cancella pass e scrivi il tuo codice

    scontati: dict[str: float] = {}

    for prodotto, prezzo in prodotti.items(): #prezzo - 10/100 (per fare il 10%)
        if prezzo > 20.0:
            prezzo = prezzo * 0.9 #per fare il 10%
            scontati[prodotto] = prezzo
        
    return scontati

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))



