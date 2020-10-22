import unittest

from src.pub import Pub


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("New Pub", 10, 10, "customer", "staff")

    def test_pub_has_name(self):
        self.assertEqual("New Pub", self.pub.name)

    def test_pub_has_width(self):
        self.assertEqual(10, self.pub.floor_w)

    def test_pub_has_height(self):
        self.assertEqual(10, self.pub.floor_h)

    def test_pub_has_customer(self):
        self.assertEqual("customer", self.pub.customer)

    def test_pub_has_staff(self):
        self.assertEqual("staff", self.pub.staff)
