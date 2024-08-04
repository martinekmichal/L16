import unittest
from Integer_Task1 import IntegerSet


class TestIntegerSet(unittest.TestCase):
    def setUp(self):
        self.non_empty_set = IntegerSet([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.empty_set = IntegerSet([])
        self.negative_numbers_set = IntegerSet([-1, -2, -3, -4, -5, -6, -7, -8, -9])
        self.mixed_numbers_set = IntegerSet([-1, 0, 1, 2, 3])

    def test_sum(self):
        self.assertEqual(self.non_empty_set.sum(), 15, "Chyba v součtu.")
        self.assertEqual(self.empty_set.sum(), 0, "Chyba v součtu prázdná data")
        self.assertEqual(self.negative_numbers_set.sum(), -15, "Chyba v součtu - záporná čísla")
        self.assertEqual(self.mixed_numbers_set.sum(), 5, "Chyba v součtu smíšená čísla")
    def test_mean(self):
        self.assertEqual(self.non_empty_set.mean(), 3, "Chyba v aritmetickém průměru neprázdné sady")
        with self.assertRaises(ValueError):
            self.empty_set.mean()
        self.assertEqual(self.negative_numbers_set.mean(), -3, "Chyba v aritmetickém průměru sady se zápornými čísly")
        self.assertEqual(self.mixed_numbers_set.mean(), 1, "Chyba v aritmetickém průměru smíšené sady")
    def test_maximum(self):
        self.assertEqual(self.non_empty_set.maximum(), 5, "Chyba v maximální hodnotě neprázdné sady")
        with self.assertRaises(ValueError):
            self.empty_set.maximum()
        self.assertEqual(self.negative_numbers_set.maximum(), -1, "Chyba v maximální hodnotě sady se zápornými čísly")
        self.assertEqual(self.mixed_numbers_set.maximum(), 3, "Chyba v maximální hodnotě smíšené sady")
    def test_minimum(self):
        self.assertEqual(self.non_empty_set.minimum(), 1, "Chyba v minimální hodnotě neprázdné sady")
        with self.assertRaises(ValueError):
            self.empty_set.minimum()
        self.assertEqual(self.negative_numbers_set.minimum(), -5, "Chyba v minimální hodnotě sady se zápornými čísly")
        self.assertEqual(self.mixed_numbers_set.minimum(), -1, "Chyba v minimální hodnotě smíšené sady")

if __name__ == "__main__":
    unittest.main()

