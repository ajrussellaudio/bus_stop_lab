import unittest

from bus_stop import BusStop
from person import Person

class BusStopTest(unittest.TestCase):
    def setUp(self):
        self.bus_stop = BusStop("Partick Interchange")

    def test_location(self):
        self.assertEqual(self.bus_stop.location, "Partick Interchange")

    def test_queue_length(self):
        self.assertEqual(self.bus_stop.queue_length(), 0)

    def test_add(self):
        person = Person("Alan", 35)
        self.bus_stop.add(person)
        self.assertEqual(self.bus_stop.queue_length(), 1)

    def test_remove(self):
        person1 = Person("Alan", 35)
        person2 = Person("Marj", 31)
        self.bus_stop.add(person1)
        self.bus_stop.add(person2)
        removed = self.bus_stop.remove()
        self.assertEqual(removed, person1)
        self.assertEqual(self.bus_stop.queue_length(), 1)


if __name__ == '__main__':
    unittest.main()
