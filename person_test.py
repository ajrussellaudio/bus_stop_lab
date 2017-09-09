import unittest

from person import Person

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.person = Person("Alan", 35)

    def test_name(self):
        self.assertEqual(self.person.name, "Alan")

    def test_age(self):
        self.assertEqual(self.person.age, 35)

if __name__ == '__main__':
    unittest.main()
