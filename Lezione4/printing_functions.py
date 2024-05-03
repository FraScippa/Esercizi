

def construct_rectangle(area: float) -> list[float]:
    """Calculate rectangle area"""
    height: int = int(area**0.5) 
    
    while area%height != 0:
        height -= 1
    
    base= area // height
    
    return[base, height]

#print(construct_rectangle(4))
    
#Fibonacci Sequence
def fibonacci(index: int) -> int:
    """Calculate the value of fibonacci with the index"""
    if index <= 0 :
        return 0
    
    elif index == 1:
        return 1
    
    else:
        return fibonacci(index-1) + fibonacci(index-2)

#print(fibonacci(9))


def is_subsequence(s: str, t: str) -> bool:
    """Check if a string is in another string and retun a Boolean"""
    index = 0
    index2 = 0
    
    while index < len(s) and index2 < len(t):
        
        if s[index] == t[index2]:
            index += 1
        index2 += 1
    
    return index == len(s)

#print(is_subsequence("abc", "ahbgdc"))


def moltiplication(x: float, y: float) -> float:
    """Moltiplication"""
    result: float = x*y
    
    return result


def blackjack(cards: list[int]) -> int:
    cards_sum: int = sum(cards)
    num_aces: int = cards.count(1) + cards.count(11)

    while cards_sum > 21 and num_aces > 0:
        cards_sum -= 10
        num_aces -= 1
        
    return cards_sum

#print(blackjack([1, 10, 11]))

#PRIMO MODO (PIù LENTO)
def  construct_retangle(area: float) -> list[float]:
    combos = []
    for larghezza in range(1, area + 1): #cicli annidati, i rimane fermo e j divent ogni valore. Provi tute le possibilità (non molto veloce)
        for altezza in range(1, area +1):
            if larghezza * altezza == area and larghezza >= altezza:
                combos.append([larghezza, altezza])
                #return [larghezza, altezza]
    #combos = [[1,4],[2,2],[4,11]]
    max_diff: float = float('inf') #gli dico di prendere il n più grande di questa macchina
    index_diff: int = 0 #enuerate combinazione indice e elemento
    
    for i, combo in enumerate(combos): #dopo questo for trovo la diff più piccola e l'indice collegato
        curr_diff: float = combo[0] - combo[1] #se non volessi usare enumerate: for i in range(len(combos))
        if curr_diff <= max_diff:                                               # combos[i][0] - combos[i][1]
            min_diff = curr_diff
            index_diff = i

    return combos[index_diff]

def  construct_retangle_optimezed(area: float) -> list[int]:
    sqrt_area = int(area ** 0,5)
    for altezza in range(sqrt_area, 0, -1):
        if area % altezza == 0:
            larghezza = area // altezza
            return [larghezza, altezza]

#Scrivi una funzione che accetta una stringa come input, rimuove le parole non significative comuni stop_words e 
#restituisce un dizionario in cui le chiavi sono parole univoche nel testo rimanente (ignorando la distinzione tra maiuscole e 
#minuscole e la punteggiatura) e i valori sono le frequenze di quelle parole.

import re 

def  word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    text = re.sub(r'[^\w\s]', '', text.lower()) #^: significa che devi iniziare da una parola e lo rimpiazzo con ''. Per eliminare la punteggiatura

    words = list()
    for word in text.split(): #per fargli prendere le parole intere
        if word not in stopwords:
            word.append(word)

#Scrivi una funzione che accetta una stringa come input, rimuove le parole non significative comuni stop_words e 
#restituisce un dizionario in cui le chiavi sono parole univoche nel testo rimanente (ignorando la distinzione tra maiuscole e 
#minuscole e la punteggiatura) e i valori sono le frequenze di quelle parole.

    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1 #se la chiave non esiste ti restituisce 0
        """if word not in result:
            result[word] = 1
        else:
            result[word] += 1"""
    
    return result

from collections import Counter

def  word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    text = re.sub(r'[^\w\s]', '', text.lower())

    words = list()
    for word in text.split(): #per fargli prendere le parole intere
        if word not in stopwords:
            word.append(word)

    result = Counter(words) #conta le parole che uguali e le mette in un dizionario 
    return dict(result)

#Immagina di avere una raccolta di note musicali rappresentate da una serie di numeri interi. 
#Queste note possono avere altezze (valori) diversi. Una sequenza armoniosa è come una melodia piacevole in cui la differenza 
#di altezza tra la nota massimale e quella minimale è uguale a 1. Ad esempio, la serie di note [3,2,2,2,3] è armoniosa, 
#perché la differenza fra 3 e 2 è 1.
#Trovare l'armonia perfetta:
#Il tuo compito è scrivere una funzione che prenda come input questa serie di note musicali (numeri). 
#La funzione dovrebbe trovare la sequenza armoniosa più lunga che puoi creare da queste note. 
#Ricorda, una sottosequenza è una selezione di note dalla lista originale che mantiene l'ordine degli elementi.
#Colpire le note giuste:
#Ad esempio, se nums è [1, 3, 2, 2, 5, 2, 3, 7], la sottosequenza armonica 
#più lunga è [3, 2, 2, 2, 3]. La funzione dovrebbe restituire 5 (la lunghezza di questa sottosequenza).

from collections import Countr

def find_1hs(notes: list[int]) -> int:
    
    num_freq = dict(Counter(notes)) #conta quante volte c'è il numero nella lista e lo mette come valore. ex: [1,3,2,2,2,5,2,3,7] 1:1 3:2 2:4 5:1
    max_length = 0
    
    for num in num_freq:
        if num + 1 in num_freq:
            somma = num_freq[num] + num_freq[num+1]
            if somma >= max_length:
                max_length = somma
            #max_length = max(max_length, num_freq[num] + num_freq[num+1])
    
    return max_length

#Immagina di avere uno scrigno pieno di gioielli (rappresentati da una lista di numeri interi). 
#Questi gioielli hanno vari valori, alcuni più preziosi di altri. 
#Il tuo compito è trovare il terzo gioiello distinto più prezioso nello scrigno.
#Qual è la svolta?
#Nello scrigno possono esserci gioielli duplicati (numeri con lo stesso valore). A noi però interessano solo valori distinti, 
#ovvero gioielli con valori unici.
#Scrivi una funzione che prenda come input questo array di valori di gioielli (numeri). 
#Se nello scrigno sono presenti almeno tre valori distinti, la funzione dovrebbe restituire il valore del 
#terzo gioiello distinto di maggior valore.
#Ma c'è un problema!
#Se non ci sono tre valori distinti (ad esempio, solo due valori univoci o tutti i valori sono uguali), 
#la funzione dovrebbe restituire il valore del gioiello più prezioso nello scrigno.

def third_max(gems: list[int]) -> int:
    gems = sorted(list(set(gems)), reverse=True)
    if len(gems) >= 3:
        return gems[2]
    else:
        return[0]
