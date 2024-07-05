class Pagamento:
    
    def __init__(self):
        pass

    def setPagamento(self, importo: float):
        self.__importo: float = round(importo,2)
        return self.__importo
    
    def getPagamento(self):
        return self.__importo
    
    def dettagliPagamento(self):
        print(f"Importo del pagamento: €{self.getPagamento()}")

class PagamentoContanti(Pagamento):


    def __init__(self):
        super().__init__()

    def dettagliPagamento(self):
        return super().dettagliPagamento()
    
    def inPezziDa(self):

        self.contanti: dict[float,int] = {500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 
                                          1:0, 0.50:0, 0.20:0, 0.10:0, 0.05:0, 0.01:0}
        
        new = self.getPagamento()
        print(f"Pagamento in contanti di: €{new}\n{new} euro da pagare in contanti con:")
        
        while new != 0:
        
            for k,v in self.contanti.items():

                if round(new,2) >= k:
                    new: float = round(new - k, 2)
                    self.contanti[k] = v+1
                    break
        
        for k,v in self.contanti.items():
            if v > 0:
                if k >= 5:
                    print(f"{v} banconote da {k} euro")
                else:
                    print(f"{v} monete da {k} euro")

class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, nome_titolare: str, data_scadenza: str, numero_carta: str):
        super().__init__()
        self.nome_titolare: str = nome_titolare
        self.data_scadenza: str = data_scadenza
        self.numero_carta: str = numero_carta

    def dettagliPagamento(self):
        s: str = ""
        s += f"Pagamento di: {self.getPagamento()} effettuato con la carta di credito"
        s += f"\nNome sulla carta: {self.nome_titolare}"
        s += f"\nData di scadenza: {self.data_scadenza}"
        s += f"\nNumero della carta: {self.numero_carta}"
        print(s)

print("ciao")