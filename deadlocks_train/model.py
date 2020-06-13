class Train:
    def __init__(self, id, length, front):
        self.id = id
        self.train_length = length
        self.front = front


class Intersection:
    def __init__(self, id, mutex, locked_by):
        self.id = id
        self.mutex = mutex
        self.locked_by = locked_by


class Crossing:
    def __init__(self, position, intersection):
        self.position = position
        self.intersection = intersection
