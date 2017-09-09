import unittest

from bus_stop import BusStop
from person import Person

class BusStopTest(unittest.TestCase):
    def setUp(self):
        self.bus_stop = BusStop("Partick Interchange")

    def test_location(self):
        self.assertEqual(self.bus_stop.location, "Partick Interchange")

if __name__ == '__main__':
    unittest.main()
