#file = open("file.txt") #è equivalente nel dire "as file". Ciò che ritorna l'open va in file

with open('file.txt') as file: #ritornerà un oggetto, quindi lo lego ad una variabile.
    pass

#file.close() #chiudi il file e lasci libera la risorsa.

class ContextManager:
    def __enter__(self):

        print('Risorsa Acquisita!')

        return self #viene chiamata e ritorna se stesso
    
    def __exit__(self, exc_type: Exception, exc_value, traseback: str):
        
        if exc_type is not None:
            pass
        print('Risorsa rilasciata')

        return False #le eccezioni vengono fatte salire al chiamante, perchè potrebbero essere gestite dalla funzione chiamante

with ContextManager() as manager: #creo l'oggetto di tipo ContextManager, dato che ho usato la keyword cercerà l'__enter__ e l'__exit__
#la variabile manager è dello stesso tipo di file -> TextIOWrapper: è il nostro ContextManager
    
    print('Sono Dentro With')