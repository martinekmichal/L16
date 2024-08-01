import unittest


def add(a, b):
    return a + b


class TestAddFunction(unittest.TestCase):

    def test_addition_positive(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(6, 7), 13)
        self.assertEqual(add(58, 73), 131)

    def test_addition_negative(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-7, -6), -13)

    def test_addition_zero(self):
        self.assertEqual(add(-2, 0), -2)
        self.assertEqual(add(2, 0), 2)
        self.assertEqual(add(-17, 0), -17)
        self.assertEqual(add(17, 0), 17)

        self.assertEqual(add(0, -2), -2)
        self.assertEqual(add(0, 2), 2)
        self.assertEqual(add(0, -17), -17)
        self.assertEqual(add(0, 17), 17)

    def test_addition_mix(self):
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(-13, 6), -7)
        self.assertEqual(add(13, -6), 7)



if __name__ == '__main__':
    unittest.main()