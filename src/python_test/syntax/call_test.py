class BingoCage:
    def __init__(self, items):
        self._items = list(items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BiogoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


def test_biongo():
    bingo = BingoCage(range(3))
    assert bingo.pick() == 2
    assert bingo() == 1
