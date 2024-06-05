

def fibonacci(n: int):
    a:int = 1
    b:int = 1
    for _ in range(n):

        c = a + b 
        a = b
        b = c
    return b

import time

a = time.time()

print(fibonacci(1000))
print(f"tempo impiegato: {time.time() - a}")