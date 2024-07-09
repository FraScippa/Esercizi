import threading
import time

def thread_function(name):
    print(f"Thread {name}: starting at {time.time()}")
    time.sleep(2)
    print(f"Thread {name}: finishing at {time.time()}")

if __name__ == "__main__":
    
    x = threading.Thread(target= thread_function, args=(1,))
    print(f"Main : before running thread")
    x.start()
    print(f"Main : wait for the thread to finish")
    print(f"Main : all done")

threads = list()

for index in range(3):
    print(f"Main : before running thread")
    x = threading.Thread(target=thread_function, args=(index,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    print(f"Main : wait the thread to finish")
    thread.join()
    print(f"Main : all done")

#with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #executor.map(thread_function, range(3))
