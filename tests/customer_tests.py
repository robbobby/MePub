import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("customer name", 17, 3, 4, 5, 100)
        self.customer2 = Customer("customer name", 18, 3, 4, 5, 100)
        self.customer3 = Customer("customer name", 40, 3, 4, 5, 100)
            ## name, age, hunger, thirst, drunk_level

    def test_customer_has_name(self):
        self.assertEqual("customer name", self.customer.name)

    def test_customer_has_age(self):
        self.assertEqual(17, self.customer.age)

    def test_customer_has_hunger(self):
        self.assertEqual(3, self.customer.hunger)

    def test_customer_has_thirst(self):
        self.assertEqual(4,self.customer.thirst)

    def test_customer_has_drunk_level(self):
        self.assertEqual(5, self.customer.drunk_level)

    def test_customer_has_naughty_level(self):
        self.assertEqual(100,self.customer.naughty_level)

    def test_customer_can_drink_alchohol(self):
        self.assertEqual(False, self.customer.is_over_18())

    def test_customer__can_drink_alchohol(self):
        self.assertEqual(True, self.customer2.is_over_18())

    def test_customer___can_drink_alchohol(self):
        self.assertEqual(True, self.customer3.is_over_18())