import unittest
from src.stock.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Tennants", 42, 499)
        self.drink_2 = Drink("Cola", 0, 299)

    def test_drink_has_name(self):
        self.assertEqual("Tennants", self.drink.name)

    def test_drink_has_units(self):
        self.assertEqual(42, self.drink.units)

    def test_drink_has_price(self):
        self.assertEqual(499, self.drink.price)

    def test_is_drink_alchoholic(self):
        self.assertEqual(True, self.drink.is_alchoholic())

    def test_is_drink__alchoholic(self):
        self.assertEqual(False, self.drink_2.is_alchoholic())
