import unittest 
from dottore import Dottore
from fattura import Fattura
from paziente import Paziente
from persona import Persona

class TestPersona(unittest.TestCase):
    
    def setUp(self):
        self.persona = Persona("Nicolò", "Di Silvestro")
    
    def test_inizializzazione(self):
        self.assertEqual(type(self.persona.getName()), str, 'il nome inserito è una stringa')
        self.assertEqual(type(self.persona.getLastname()), str, 'il cognome inserito è una stringa')
        self.assertNotEqual(self.persona.getAge(), 2, "età inserita == 0")
    
    def test_setName(self):
        self.persona.setName("Peppino")
        self.assertEqual(self.persona.getName(), "Peppino", "il nome non coincide")
    
    def test_setLastName(self):
        self.persona.setLastName("Sccalzi")
        self.assertEqual(self.persona.getLastname(), "Sccalzi", "il cognome non coincide")
    
    def test_setAge(self):
        self.persona.setAge(20)
        self.assertGreater(self.persona.getAge(), 0, "l'età è minore di 0")
        
class TestDottore(unittest.TestCase):
    
    def setUp(self):
        self.dottore = Dottore("Chirurgo", 16.50, "Giovannino", "Cicci")
    
    def test_inizializzazione(self):
        self.assertEqual(type(self.dottore.getSpecialization()), str, "la specializzazione non è una stringa")
        self.assertGreater(self.dottore.getParcel(), 0, "la parcella è minore di 0")
        self.assertEqual(type(self.dottore.getName()), str, "il nome non è una stringa")
        self.assertNotEqual(type(self.dottore.getLastname()), int, "il cognome non è un intero")
    
    def test_isValidDoctor(self):
        self.assertFalse(self.dottore.isAValidDoctor(), False)
        self.dottore.setAge(32)
        self.assertTrue(self.dottore.isAValidDoctor(), True)
    
class TestPaziente(unittest.TestCase):
    
    def setUp(self):
        self.paziente = Paziente("21021", "Enzo", "Montanelli")
        self.persona = Persona("Nicolò", "Di Silvestro")
        
    def test_inizializzazione(self):
        self.assertNotEqual(type(self.paziente.getIdCode()), float, "il codice ID deve essere un intero")
        self.assertEqual(type(self.paziente.getName()), str, "il nome deve essere una stringa")
        self.assertIsNotNone(self.paziente.getLastname(), "il cognome è diverso da None")
    
class TestFattura(unittest.TestCase):
    
    def setUp(self):
        self.doc1 = Dottore("Chirurgo", 16.50, "Giovannino", "Cicci")
        self.doc1.setAge(38)
        self.p1 = Paziente("343535", "Nicolò", "Di Silvestro")
        self.p2 = Paziente("433214", "Christian", "Ciota")
        self.fattura = Fattura([self.p1],self.doc1)
    
    def test_inizializzazione(self):
        self.assertEqual(self.fattura.getSalary(), 16.5, "il risultato non è corretto")
        self.assertNotEqual(self.fattura.getFatture(), 0, "il risultato è 0")
        
    def test_modifiche_liste(self):
        self.fattura.addPatient(self.p2)
        self.assertEqual(self.fattura.patient[1], self.p2, "il paziente non è corretto")
        self.fattura.removePatient("343535")
        self.assertNotEqual(self.fattura.patient[0], self.p1, "il paziente ancora esiste nella lista")
        
if __name__ == '__main__':
    unittest.main()