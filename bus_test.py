import unittest
from bus import Bus
from person import Person

class BusTest(unittest.TestCase):
    def setUp(self):
        self.bus = Bus("77", "Braehead")

    def test_route_number(self):
        self.assertEqual(self.bus.route_number, "77")

    def test_destination(self):
        self.assertEqual(self.bus.destination, "Braehead")

    def test_drive(self):
        self.assertEqual(self.bus.drive(), "Vroom vroom")

    def test_passengers(self):
        self.assertEqual(self.bus.passenger_count(), 0)

    def test_pick_up(self):
        passenger = Person("Alan", 35)
        self.bus.pick_up(passenger)
        self.assertEqual(self.bus.passenger_count(), 1)

    def test_drop_off(self):
        passenger = Person("Alan", 35)
        self.bus.pick_up(passenger)
        self.bus.drop_off(passenger)
        self.assertEqual(self.bus.passenger_count(), 0)

    def test_empty(self):
        self.bus.pick_up(Person("Alan", 35))
        self.bus.pick_up(Person("Marj", 31))
        self.bus.empty()
        self.assertEqual(self.bus.passenger_count(), 0)


if __name__ == '__main__':
    unittest.main()
