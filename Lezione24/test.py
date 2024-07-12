

def codifica_signolo(car: str):
    #import string
    #alfabeto: str = string.ascii_lowercase 
    alfabeto: list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if car.lower() in alfabeto:
        index = alfabeto.index(car.lower())
        return index
    
print(codifica_signolo("o"))

def codifica(mess_codificare: str):
    s = ''
    for c in mess_codificare:
        mess = str(codifica_signolo(c))
        s += f' {mess}'
    return s

def decodifica(testo_codificato: str):
    alfabeto: list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    dec: list[int] = []
    for c in testo_codificato:
        mess = int(testo_codificato.strip())
        dec.append(mess)
        
    
    return dec

print(codifica("Bye"))
print(decodifica("1244"))