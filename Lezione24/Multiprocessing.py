from multiprocessing import Process
import time

def sleep():
    print(f"Sono nella funzione")
    time.sleep(60)
    print(f"Sto ucendo dalla funzione")

def bubble_sort_v2():
    from random import randint

    x = [randint(0, 10000)for _ in range(500000)]

    ho_fatto_swap: bool = True
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                # swap(x[j], x[j+1])
                ho_fatto_swap = False
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
        if ho_fatto_swap:
            break

if __name__ == "__main__": # queste istruzioni si eseguono solo se fai runnare questo file, se lo importi non verranno importate.
    tic: float = time.time()
    t1 = Process(target = bubble_sort_v2) 
    t2 = Process(target = bubble_sort_v2)
    t1.start()      # mi calcolo quanto ci mettono entrambi i processi a terminare (mi dovrei aspettare 60sec, e invece sono 0.004)
    t2.start()      # il processo padre ha eseguito tutto. 
    t1.join()       # per evitare questa cosa si mette il .join(). Il .join attende che entrambi i processi siano terminati
    t2.join()
    toc: float= time.time()
    time_elapsed: float = toc - tic
    
    print(f"{time_elapsed}")