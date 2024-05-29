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
                lista[T] = 'T'
            if lista[H] in ostacoli:
                lista[H] = H - v
                lista[H] = 'H'
        
        for k,v in bonus.items():
            if lista[T] in bonus:
                lista[T] = T + v
                lista[T] = 'T'
            if lista[H] in bonus:
                lista[H] = H + v
                lista[H] = 'H'
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
        if 1 <= die <= 2 and stamina < 90:
            if stamina < 90:
                H = 0
                print("Lepre!Non si muove")
                stamina +=10
            else:
                print("The Lepre, doesn't have enough stamina")  
            
        elif 3 <= die <= 4:
            if stamina >= 15:
                print("Lepre!Avanza di 9")
                H += 9
                stamina -= 15
            else:
                print("The Lepre, doesn't have enough stamina")
                
        elif die == 5:
            if H > 12 and stamina >= 20:
                H -= 12
                stamina -= 20
                print("Lepre!Arretra di 12 quadrati")
            else:
                H = H
                print("The Lepre, doesn't have enough stamina")
        
        elif 6 <= die <= 8:
            if stamina >= 5:
                H += 1
                stamina -= 5
                print("Lepre!Avanza di 1 quadrato.")
            else:
                print("The Lepre, doesn't have enough stamina")
        
            if H > 2 and stamina >= 8:
                H -= 2
                stamina -= 8
                print("Lepre!Arretra di 2 quadrati")
            else:
                H = H
                print("The Lepre, doesn't have enough stamina")
        else:
            H = 0
            
    elif H >= 70:
        H = 70
    
    return H

def meteo(T,H):
    
    if T % 10 == 0 and H % 10 == 0:
        t: int =  random.randint(1,2)
        if t == 1:
            T -= 1
            H -= 2
            print("It's raining!")
        elif t == 2:
            print('Sunny day!')
        return T,H
    
print("BANG !!!!! AND THEY'RE OFF !!!!!")

T = 0
H = 0

while True:
    
    position(T,H)
    T = tartaruga(T)
    H = lepre(H)
    meteo(T,H)
    if T == 70:
        break
    if H == 70:
        break

if T > H:
   print("TORTOISE WINS! || VAY!!!")
elif T == H:
    print("IT'S A TIE.")
else:
    print("HARE WINS || YUCH!!!")