import random

def position(T,H) -> None:
    lista: list = []
    for i in range(0,71):
        lista.append("-")
    
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
    
    ostacoli: dict = {lista[15]: 3, lista[30]: 5, lista[45]: 7}
    bonus: dict = {lista[10]: 5, lista[25]: 3, lista[50]: 10}
    
    if T < 70 and H < 70:
        for k,v in ostacoli.items():
            if lista[T] in ostacoli:
                lista[T] = T - v
            if lista[H] in ostacoli:
                lista[H] = H - v
        
        for k,v in bonus.items():
            if lista[T] in bonus:
                lista[T] = T + v
            if lista[H] in bonus:
                lista[H] = H + v
        
    print(lista)
    

def tartaruga(T) -> int:
    die: int = random.randint(1,10)
    stamina: int = 100
    if T < 70 and stamina <= 100:
        if 1 <= die <= 5:
            T += 3
            stamina -= 5
            print("Tartaruga!Avanza di 3 quadrati!")
            if stamina <= 0:
                stamina +=10
        
        elif 6 <= die <= 7 and stamina <= 100:
            T += 1
            stamina -= 3
            print("Tartaruga!Avanza di 1 quadrato!")
            if stamina <= 0:
                stamina +=10
            
        else:
            if T > 6 and stamina <= 100:
                T -= 6
                stamina -= 10
                print("Tartaruga!Arretra di 6 quadrati.")
                if stamina <= 0:
                    stamina +=10
            else:
                T = 1
                
    elif T >= 70:
        T = 70
    return T

def lepre(H) -> int:
    die: int = random.randint(1,10)
    stamina: int = 100
    
    if H < 70 and stamina <= 100:
        if 1 <= die <= 2 and stamina < 100:
            H = 0
            print("Lepre!Non si muove")
            if stamina + 10 < 100:
                stamina +=10
            else:
                print("The Lepre, dosen't have enough stamina")  
            
        elif 3 <= die <= 4 and stamina < 100:
            H += 9
            print("Lepre!Avanza di 9")
            stamina -= 15
            if stamina < 15:
                print("The Lepre, dosen't have enough stamina")  
        elif die == 5 and stamina < 100:
            if H > 12:
                H -= 12
                print("Lepre!Arretra di 12 quadrati")
                stamina -= 20
            elif stamina < 20:
                H = 1
                print("The Lepre, dosen't have enough stamina")
        
        elif 6 <= die <= 8 and stamina < 100:
            H += 1
            print("Lepre!Avanza di 1 quadrato.")
            stamina -= 5
        else:
            if H > 2 and stamina < 100:
                H -= 2
                print("Lepre!Arretra di 2 quadrati")
                stamina -= 8
            else:
                H = 1
            
    elif H >= 70:
        H = 70
    
    return H

def meteo(T,H):
    if T % 10 == 0 or H % 10 == 0:
        t: int =  random.randint(1,2)
        if t == 1:
            print("It's raining!")
            T -= 1
            H -= 2
        elif t == 2:
            print('Sunny day!')
    
print("BANG !!!!! AND THEY'RE OFF !!!!!")

T = 0
H = 0

while T < 70 or H < 70:
    position(T,H)
    meteo(T,H)
    T = tartaruga(T)
    H = tartaruga(H)


if T > H:
   print("TORTOISE WINS! || VAY!!!")
elif T == H:
    print("IT'S A TIE.")
else:
    print("HARE WINS || YUCH!!!")
    





