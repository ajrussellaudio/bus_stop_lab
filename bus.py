class Bus():
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.__passengers = []

    def drive(self):
        return "Vroom vroom"

    def passenger_count(self):
        return len(self.__passengers)

    def pick_up(self, passenger):
        self.__passengers.append(passenger)

    def drop_off(self, passenger):
        self.__passengers.remove(passenger)
