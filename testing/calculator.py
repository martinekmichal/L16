import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class TestCalculatorMethods(unittest.TestCase):
    def setUp(self):
        # Inicializácia inštancie kalkulačky pre každý test
        self.calculator = Calculator()


    def test_add(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8, "Sčítanie nefunguje správne")

        result = self.calculator.add(-3, 5)
        self.assertEqual(result, 2, "Sčítání záporného čísla nefunguje správně")

        result = self.calculator.add(3, -5)
        self.assertEqual(result, -2, "Sčítání záporného čísla nefunguje správně")

        result = self.calculator.add(-3, -5)
        self.assertEqual(result, -8, "Sčítání záporných čísel nefunguje správně")

    def test_subtract(self):
        result = self.calculator.subtract(10, 4)
        self.assertEqual(result, 6, "Odčítanie nefunguje správne")

        result = self.calculator.subtract(-5, 3)
        self.assertEqual(result, -8, "Odčítání ze záporným číslem nefunguje správně")

        result = self.calculator.subtract(5, -3)
        self.assertEqual(result, 8, "Odčítání záporného čísla nefunguje správně")

        result = self.calculator.subtract(-5, -3)
        self.assertEqual(result, -2, "Odčítání záporných čísel nefunguje správne")




    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6, "Násobenie nefunguje správne")

        result = self.calculator.multiply(-2, 3)
        self.assertEqual(result, -6, "Násobení záporného čísla a kladného čísla nefunguje správně")

        result = self.calculator.multiply(2, -3)
        self.assertEqual(result, -6, "Násobení kladného čísla a záporného čísla nefunguje správně")

        result = self.calculator.multiply(-2, -3)
        self.assertEqual(result, 6, "Násobení dvou záporných čísel nefunguje správně")


        result = self.calculator.multiply(0, 0)
        self.assertEqual(result, 0, "Násobení nuly nefunguje správně")

        result = self.calculator.multiply(0, 5)
        self.assertEqual(result, 0, "Násobení nuly a kladného čísla nefunguje správně")

        result = self.calculator.multiply(5, 0)
        self.assertEqual(result, 0, "Násobení kladného čísla a nuly nefunguje správně")


    def test_divide(self):
        result = self.calculator.divide(8, 2)
        self.assertEqual(result, 4, "Delenie nefunguje správne")

        result = self.calculator.divide(0, 5)
        self.assertEqual(result, 0, "Dělení nuly nefunguje správně")

        result = self.calculator.divide(-10, 2)
        self.assertEqual(result, -5, "Dělení záporného čísla a kladného čísla nefunguje správně")


        # Test delenia nulou
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)


if __name__ == '__main__':
    unittest.main()