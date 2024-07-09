
# i decorator sono funzioni che prendono come argomento altre funzioni, ne estendono la funzionalità SENZA MODIFICARE LA FUNZIONE DI BASE
def divisione_intelligente(funzione_base): 
   def interna(num1, num2): # come verrà estesa la funzione base
      if num2 == 0:
         print("Non puoi dividere per zero!")
         return
      
      return funzione_base(num1, num2)
   return interna

# usiamo il nostro decorator
@divisione_intelligente 
def divisione(num1: int, num2: int):
   return num1 / num2