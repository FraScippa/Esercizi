import unittest
from Lezione10Classi import Calculation

class TestCalc(unittest.TestCase):
    
    def test_sum(self):
        
        calc_1 = Calculation(a=2, b=3)
        result = calc_1.get_sum()
        self.assertEqual(result, 5, msg = f'Errore Test Failed the goal was 5 the function returned {result}')

    def test_prod(self):

        calc_1 = Calculation(a =2, b=3)
        result = calc_1.get_product()
        self.assertEqual(result, 6, msg = f'Errore Test Failed the goal was 5 the function returned {result}')

    def test_quotient(self):

        calc_1 = Calculation(a =2, b=3)
        result = calc_1.get_quotient()
        self.assertEqual(result, 2/3, msg = f'Errore Test Failed the goal was 5 the function returned {result}')

if __name__ == '__main__': #se la variabile 'name' è uguale alla dicitura 'main'.Se viene importato non viene eseguito

    unittest.main()        #ti permette di eseguire questa linea di codice, dopo aver esequito il file, se non viene eseguito viene ignorato
