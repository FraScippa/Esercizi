import random

def position(T,H) -> None:
    
    lista: list = []
    
    for i in range(0,71):
        lista.append(f"{i} -")
    
    if T < 70:
        lista[T] = 'T'
    else:
        T = 70
    if H < 70:
        lista[H] = 'H'
    else:
        H = 70
    if T == H:
        lista[T] = 'Ouch!'
    
    print(lista)

def tartaruga(T) -> int:
    
    die: int = random.randint(1,10)
    if T < 70:
        if 1 <= die <= 5:
            T += 3
            print("Tartaruga!Avanza di 3 quadrati!")
            
        elif 6 <= die <= 7:
            T += 1
            print("Tartaruga!Avanza di 1 quadrato!")
            
        else:
            if T > 6:
                T -= 6
            else:
                T = 1 
            print("Tartaruga!Arretra di 6 quadrati.")
    elif T >= 70:
        T = 70    
    
    return T

def lepre(H) -> int:
    
    die: int = random.randint(1,10)
    if H < 70:
        if 1 <= die <= 2:
            H = 0
            print("Lepre!Non si muove")
            
        elif 3 <= die <= 4:
            H += 9
            print("Lepre!Avanza di 9")
            
        elif die == 5:
            if H > 12:
                H -= 12
            else:
                H = 1
            print("Lepre!Arretra di 12 quadrati")
        
        elif 6 <= die <= 8:
            H += 1
            print("Lepre!Avanza di 1 quadrato.")
        
        else:
            if H > 2:
                H -= 2
            else:
                H = 1
            print("Lepre!Arretra di 2 quadrati")
    elif H >= 70:
        H = 70
    
    return H

print("BANG !!!!! AND THEY'RE OFF !!!!!")

T = 0
H = 0

while T < 70 or H < 70:
    
    position(T,H)
    
    T = tartaruga(T)
    H = tartaruga(H)


if T > H:
    
    print("TORTOISE WINS! || VAY!!!")
elif T == H:
    print("IT'S A TIE.")
else:
    print("HARE WINS || YUCH!!!")
    





