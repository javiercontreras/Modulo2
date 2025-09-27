import unittest
from calculadora import Calculadora

class TestSimpleCalculadora(unittest.TestCase):
    #Se crea el objeto calculadora para la clase
    @classmethod
    def setUpClass(cls):
        cls.calculadora = Calculadora()
        print("setUp: Calculadora inicializada")
    # setUp se ejecuta antes de cada método de prueba


    def test_suma(self):
        self.assertEqual(self.calculadora.suma(1,2),3)

    # Usando assertRaises como gestor de contexto (método recomendado)
    def test_division_cero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculadora.div(1,0)
    
    # verificar que un error no se lanza en casos normales
    def test_division_correcta(self):
        resultado = self.calculadora.div(10, 2)
        self.assertEqual(resultado, 5)

if __name__ == '__main__':
    unittest.main()
