from Task1_Integerset import IntegerSet
import unittest

class TestIntegerSet(unittest.TestCase):
    def setUp(self):
        # Inicializace několika instancí IntegerSet pro každý test
        self.neprazdna_sada = IntegerSet([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.prazdna_sada = IntegerSet([])
        self.zaporne_cisla_sada = IntegerSet([-1, -2, -3, -4, -5, -6, -7, -8, -9])
        self.smiseny_cisla_sada = IntegerSet([-1, 0, 1, 2, 3, 4])
    def test_soucet(self):
        self.assertEqual(self.neprazdna_sada.soucet(), 45, "Chyba v součtu neprázdné sady")
        self.assertEqual(self.prazdna_sada.soucet(), 0, "Chyba v součtu prázdné sady")
        self.assertEqual(self.zaporne_cisla_sada.soucet(), -45, "Chyba v součtu sady se zápornými čísly")
        self.assertEqual(self.smiseny_cisla_sada.soucet(), 9, "Chyba v součtu smíšené sady")
