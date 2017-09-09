class BusStop():
    def __init__(self, location):
        self.location = location
        self.queue = []

    def queue_length(self):
        return len(self.queue)

    def add(self, person):
        self.queue.append(person)

    def remove(self):
        return self.queue.pop(0)
