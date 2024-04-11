import unittest
from app import hola_mundo

class TestHolaMundo(unittest.TestCase):
    def test_hola_mundo(self):
        resultado_esperado = "¡Hola Mundo!"
        resultado_real = hola_mundo()
        self.assertEqual(resultado_real, resultado_esperado)
 
if __name__ == "__main__":
    unittest.main()
