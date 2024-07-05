class Documento:
    
    def __init__(self, text: str):
        self.text: str = text

    def getText(self):
        return self.text
    
    def setText(self, text_new: str):
        self.text: str = text_new
        return self.text
    
    def isInText(self, word: str):
        if word in self.getText():
            return True
        else:
            return False
        
class Email(Documento):

    def __init__(self, mittente: str, destinatario: str, titolo: str, text: str):
        self.mittente: str = mittente
        self.destinatario: str = destinatario
        self.titolo: str = titolo
        super().__init__(text)

    def getMittente(self):
        return self.mittente
    
    def getDestinatario(self):
        return self.destinatario
    
    def getTitolo(self):
        return self.titolo
    
    def setMittente(self, new_mittente: str):
        self.mittente: str = new_mittente
        return self.mittente
    
    def setDestinatario(self, new_destinatario: str):
        self.destinatario: str = new_destinatario
        return self.destinatario
    
    def setTitolo(self, new_titolo: str):
        self.titolo: str = new_titolo
        return self.titolo
    
    def writeToFile(self, nome_file: str) -> str:
        with open(nome_file, 'w') as doc:
            return doc.write(self.text)
        
    def getText(self) -> str:
        s: str = ""
        s+= f"\nDa: {self.getMittente()}, A: {self.getDestinatario()}\n"
        s+= f"Titolo: {self.getTitolo()}\n"
        s+= f"Messaggio: {self.text}"
        return s
    
class File(Documento):

    def __init__(self, nomePercorso: str):
        self.nomePercorso: str = nomePercorso

    def leggiTestoDaFile(self):
        with open(self.nomePercorso,"r") as doc:
            return doc.read()
    
    def getText(self) -> str:
        s: str = ""
        s += f"Percorso: {self.nomePercorso}\n"
        s += f"Contenuto: {self.leggiTestoDaFile()}"
        return s


email: Email = Email("alice@example.com","bob@example.com","Incontro","Ciao Bob, possiamo incontrarci domani?")
file: File = File("documento.txt") 

print(email.getText())
print(file.getText())

email.writeToFile('email1.txt')

print(email.isInText("incontrarci"))
print(email.isInText("percorso"))
   