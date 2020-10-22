import unittest

from src.stock.ingredient import Ingredient


class TestIngredient(unittest.TestCase):
    def setUp(self):
        self.ingredient = Ingredient("Egg", 1, 10)

    def test_ingredient_has_name(self):
        self.assertEqual("Egg", self.ingredient.name)

    def test_ingredient_has_base_price(self):
        self.assertEqual(1, self.ingredient.base_price)

    def test_ingredient_has_quality(self):
        self.assertEqual(10, self.ingredient.quality)
