from Task1_Integerset import IntegerSet
import unittest

class TestIntegerSet(unittest.TestCase):
    def setUp(self):
        # Inicializace několika instancí IntegerSet pro každý test
        self.kladna_neprazdna_sada = IntegerSet([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.prazdna_sada = IntegerSet([])
        self.zaporne_cisla_sada = IntegerSet([-1, -2, -3, -4, -5, -6, -7, -8, -9])
        self.smiseny_cisla_sada = IntegerSet([-1, 0, 1, 2, 3, 4])
    def test_soucet(self):
        self.assertEqual(self.kladna_neprazdna_sada.soucet(), 45, "Chyba v součtu kladných čísel.")
        self.assertEqual(self.prazdna_sada.soucet(), 0, "Chyba v součtu prázdné sady.")
        self.assertEqual(self.zaporne_cisla_sada.soucet(), -45, "Chyba v součtu se zápornými čísly.")
        self.assertEqual(self.smiseny_cisla_sada.soucet(), 9, "Chyba v součtu smíšených čísel.")
    def test_prumer(self):
        self.assertEqual(self.kladna_neprazdna_sada.prumer(), 5, "Chyba v průměru s kladnými čísly.")
        with self.assertRaises(ValueError):
            self.prazdna_sada.prumer()
        self.assertEqual(self.zaporne_cisla_sada.prumer(), -5, "Chyba v průměru se zápornými čísly.")
        self.assertEqual(self.smiseny_cisla_sada.prumer(), 1.5, "Chyba v průměru se smíšenými čísly.")
    def test_maximum(self):
        self.assertEqual(self.kladna_neprazdna_sada.maximum(), 9, "Chyba v maximální hodnotě s kladnými čísly.")
        with self.assertRaises(ValueError):
            self.prazdna_sada.maximum()
        self.assertEqual(self.zaporne_cisla_sada.maximum(), -1, "Chyba v maximální hodnotě se zápornými čísly.")
        self.assertEqual(self.smiseny_cisla_sada.maximum(), 4, "Chyba v maximální hodnotě se smíšenými čísly.")
    def test_minimum(self):
        self.assertEqual(self.kladna_neprazdna_sada.minimum(), 1, "Chyba v minimální hodnotě s kladnými čísly.")
        with self.assertRaises(ValueError):
            self.prazdna_sada.minimum()
        self.assertEqual(self.zaporne_cisla_sada.minimum(), -9, "Chyba v minimální hodnotě se zápornými čísly.")
        self.assertEqual(self.smiseny_cisla_sada.minimum(), -1, "Chyba v minimální hodnotě smíšené sady.")
