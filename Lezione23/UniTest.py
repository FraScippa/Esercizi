import unittest
from Lezione23 import Documento, Email, File

class TestDocumento(unittest.TestCase):

    def setUp(self):
        self.documento: Documento = Documento("Ciao Bob, possiamo incontrarci domani?")
    
    def test_inizio(self):
        self.assertEqual(type(self.documento.getText()), str, "Il documento non è un testo")
        self.assertEqual(self.documento.setText("ciao"), "ciao", "Il testo non è stato modificato correttamente")
        self.assertEqual(self.documento.isInText("c"), True, "Non, si trova nel testo.")

class TestEmail(unittest.TestCase):

    def setUp(self):
        self.email: Email = Email("alice@example.com","bob@example.com","Incontro","Ciao Bob, possiamo incontrarci domani?")

    def test_inizio(self):
        self.assertIsNotNone(self.email.getText(), "email.getText non funziona correttamente.")
        with open("email1.txt","r") as doc:
            self.assertEqual(self.email.getText(),doc.read(), "non funziona")
        self.assertTrue(self.email.isInText("domani"), "isInText non funziona correttamente")

class TestFile(unittest.TestCase):

    def setUp(self):
        self.file: File = File("documento.txt")

    def test_inizio(self):
        self.assertIsNotNone(self.file.getText(),"file.getText non funziona correttamente")
        self.assertFalse(self.file.isInText("ao"), "file.isInText non funziona correttamente")

if __name__ == '__main__':
    unittest.main()