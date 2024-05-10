#Francesca Scippa

#02-05-2024

#Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a 
#seconda del parametro to_fahrenheit. Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.

def convert_temperature(f: float, c: bool = True) -> float:
    # cancella ... e definisci i parametri della funzione, successivamente cancella pass e scrivi il tuo codice
   
    if c != True:
        to_fahrenheit = (f-32)*5/9
    else:
        to_fahrenheit = (f*9/5)+32
         
    
    return to_fahrenheit

#Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

def frequency_dict(elements: list) -> dict:
    # cancella pass e scrivi il tuo codice
    
    diz: dict = {}
    
    value = 0
    
    for fruit in elements:
        if fruit in diz:
            diz[fruit] += 1 
        else:
            diz[fruit] = 1
    return diz
    
#print(frequency_dict(['mela', 'banana', 'mela']))

#La funzione dovrebbe determinare se un elemento è presente in una lista.
#Un errore nell'implementazione porta a risultati inaspettati.
 
#TROVA L'ERRORE E CORREGGI IL CODICE

def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if element in lst:
            return True
        else:
            return False

#Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.

def list_statistics(numbers: list[int]) -> int :
    # cancella ... e definisci il tipo del dato di ritorno, successivamente cancella pass e scrivi il tuo codice
    
    numbers.sort()
    
    n_max: int = numbers[-1]
    n_min: int = numbers[0]
    
    somma = sum(numbers)
    media = somma/len(numbers)
    
    result= n_max, n_min, media
    
    return result

#Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
#La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e 
#l'elemento iniziale viene spostato alla fine della lista. 
#Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.

def rotate_left(elements: list[int], k: int) -> list[int]:
    # cancella pass e scrivi il tuo codice
   
    lunghezza: int = len(elements)
    rotated = []
    
    if k > lunghezza:
        k = k % lunghezza #ricalcolo il nuovo valore di k. il resto della divisione sarà il numero di quante posizioni si sposteranno i numeri.       
    rotated = elements[k:] + elements[:k] #questa operazione si "attiva" quando lo spostamento è più grande della lista, per evitare l'errore.
    #spostiamo gli elementi
    
    return rotated 

#Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

def sum_above_threshold(numbers: list[int], t: int) -> int:
    # prima cancella ... e definisci parametro e tipo per il dato mancante
    # successivamente cancella pass e scrivi il tuo codice
    lista: list = []
    
    for n in numbers:
        if n > t:
            lista.append(n)
          
    somma: int = sum(lista)
        
    return somma

#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
 
def check_parentheses(expression: str) -> bool:
    # cancella pass e scrivi il tuo codice
    car: list = []
    count = 0
    for let in expression:
        if let == '(':
            count += 1
        elif let == ')':
            count -= 1
            
        if count < 0:
            return False
            
    return count == 0

#Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
#Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

def count_isolated(lista: list) -> int:
    # cancella ... e definisci parametri e tipo di dato, successivamente cancella pass e scrivi il tuo codice
    i = 0
    if lista == []:
        return i 
    else:
        for x in range(1, len(lista)-1):
            if lista[x-1] != lista[x] and lista[x] != lista[x+1]:
                i += 1
        if lista[0] != lista[1]:
            i += 1
        if lista[-1] != lista[-2]:
            i += 1
        if lista == []:
            i == 0
        return i

#Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
#ritorni un nuovo insieme senza i numeri specificati nella lista.

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    # cancella pass e scrivi il tuo codice
    
    new_set: set = set()
    
    for x in original_set:
        if x not in elements_to_remove:
            new_set.add(x)
            
    return new_set

#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # cancella pass e scrivi il tuo codice
    
    dict3 = dict1
   
    for key, value in dict2.items():  
        if key in dict3:
            dict3[key] += value
        else:
            dict3[key] = value
            
    return dict3

