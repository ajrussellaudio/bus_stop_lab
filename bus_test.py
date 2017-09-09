import unittest
from bus import Bus

class BusTest(unittest.TestCase):
    def setUp(self):
        self.bus = Bus("77", "Braehead")

    def test_route_number(self):
        self.assertEqual(self.bus.route_number, "77")

    def test_destination(self):
        self.assertEqual(self.bus.destination, "Braehead")

    def test_drive(self):
        self.assertEqual(self.bus.drive(), "Vroom vroom")

if __name__ == '__main__':
    unittest.main()
