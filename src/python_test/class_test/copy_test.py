import copy


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def test_copy():
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)

    id1 = id(bus1)
    id2 = id(bus2)
    id3 = id(bus3)

    assert id1 != id2 and id1 != id3

    bus1.drop("Bill")


class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def test_action():
    bus1 = HauntedBus(['Alice', 'Bill'])
    assert bus1.passengers == ['Alice', 'Bill']

    bus1.pick("Charlie")
    bus1.drop("Alice")
    print(bus1.passengers)

    bus2 = HauntedBus()
    bus2.pick('Carrie')
    print(bus2.passengers)

    bus3 = HauntedBus()
    print(bus3.passengers)
