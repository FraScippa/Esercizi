#Francesca Scippa

#24.04.2024

#Sei un detective esperto nel mondo dei testi e un caso sconcertante è arrivato sulla tua scrivania. Due stringhe, s e t, sono i tuoi sospettati. La tua missione: determinare se s si nasconde in bella vista all'interno di t, ma con una svolta!
#Qual è il problema?
#Non puoi semplicemente confrontare le stringhe lettera per lettera. 
#Immagina che s sia un personaggio subdolo che cerca di confondersi tra la folla (t). 
#Potrebbero camuffarsi nascondendosi tra altri personaggi, ma non cambiano mai il loro ordine! 
#Quindi, "ace" può intrufolarsi in "abcde" (rimuove semplicemente "b" e "d"), 
#ma "aec" non funzionerebbe (l'ordine cambia).

#Scrivi una funzione di interruzione del codice che prenda la stringa s (il carattere subdolo) e 
#t (la folla) come input. Se è possibile trovare s in agguato all'interno di t mantenendo il suo 
#travestimento (ordine), restituisce True. Altrimenti restituisce False. 
#Dimostra le tue abilità da detective e svela la verità nascosta!

def is_subsequence(s: str, t: str) -> bool:
    
    ind = 0
    ind2 = 0
    
    while ind < len(s) and ind2 < len(t):
        
        if s[ind] == t[ind2]:
            ind += 1
        ind2+=1
    
    return ind == len(s)
    
print(is_subsequence("abc", "ahbgdc"))
print(is_subsequence("axc", "ahbgdc"))
print(is_subsequence("abc", "abcde"))
print(is_subsequence("abc", "abecfd"))
print(is_subsequence("abc", "cab"))
print(is_subsequence("", "ahbgdc"))
print(is_subsequence("abc", ""))
print(is_subsequence("", ""))


#Immagina di avere una raccolta di note musicali rappresentate da una serie di numeri interi. 
#Queste note possono avere altezze (valori) diversi. 
#Una sequenza armoniosa è come una melodia piacevole in cui la differenza di altezza tra la nota massimale e quella minimale è uguale a 1. 
#Ad esempio, la serie di note [3,2,2,2,3] è armoniosa, perché la differenza fra 3 e 2 è 1.

#Trovare l'armonia perfetta:

#Il tuo compito è scrivere una funzione che prenda come input questa serie di note musicali (numeri). 
#La funzione dovrebbe trovare la sequenza armoniosa più lunga che puoi creare da queste note. 
#Ricorda, una sottosequenza è una selezione di note dalla lista originale che mantiene l'ordine degli elementi.

#Colpire le note giuste:

#Ad esempio, se nums è [1, 3, 2, 2, 5, 2, 3, 7], 
#la sottosequenza armonica più lunga è [3, 2, 2, 2, 3]. 
#La funzione dovrebbe restituire 5 (la lunghezza di questa sottosequenza).

#For example:

#Test	                                       Result
#print(find_lhs([1,3,2,2,5,2,3,7]))               5                                                  
#print(find_lhs([1,2,3,4]))                       2

def find_lhs(nums: list[int]) -> int:
    
    freq = {}
    
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    max_length = 0
    
    # Iteriamo attraverso le frequenze per trovare la lunghezza massima della sottosequenza armoniosa
    for num in freq:
        if num + 1 in freq:
            max_length = max(max_length, freq[num] + freq[num + 1])
    
    return max_length

print(find_lhs([1,2,3,4]))
print(find_lhs([1,3,2,2,5,2,3,7]))

    


