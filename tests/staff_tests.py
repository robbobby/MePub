import unittest
from src.staff import Staff

class TestStaff(unittest.TestCase):

    def setUp(self):
        self.staff_member = Staff("staff_name", 2, 3, ["bob", "george"], "Nothing")

    def test_staff_has_name(self):
        self.assertEqual("staff_name", self.staff_member.name)

    def test_staff_has_tiredness(self):
        self.assertEqual(2, self.staff_member.tiredness)

    def test_staff_has_stress(self):
        self.assertEqual(3, self.staff_member.stress)

    def test_staff_has_friends(self):
        self.assertEqual(2, len(self.staff_member.friends))

    def test_staff_has_wants(self):
        self.assertEqual("Nothing", self.staff_member.wants)

    def test_staff_initalised_abilities(self):
        self.assertIsNotNone(self.staff_member.bar_man_experience)
        self.assertIsNotNone(self.staff_member.bar_man_natural)
        self.assertIsNotNone(self.staff_member.bar_man_training)
        self.assertIsNotNone(self.staff_member.chef_experience)
        self.assertIsNotNone(self.staff_member.chef_natural)
        self.assertIsNotNone(self.staff_member.chef_training)
        self.assertIsNotNone(self.staff_member.waitress_experience)
        self.assertIsNotNone(self.staff_member.waitress_training)
        self.assertIsNotNone(self.staff_member.waitress_natural)

