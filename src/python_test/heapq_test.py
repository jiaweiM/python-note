import heapq as hq
import random


def test_nsmallest():
    ints = [3, 5, 6, 2, 1]
    low3 = hq.nsmallest(3, ints)
    assert low3 == [1, 2, 3]


def test_nlargest():
    ints = [3, 5, 6, 2, 1]
    top2_nums = hq.nlargest(2, ints)
    assert top2_nums == [6, 5]


def test_heappush():
    init_list = [2, 5, 1, 8, 3]
    heap = []
    [hq.heappush(heap, x) for x in init_list]
    assert heap[0] == 1


def test_heappop():
    init_list = [2, 5, 1, 8, 3]
    heap = []
    [hq.heappush(heap, x) for x in init_list]
    assert heap[0] == 1
    assert hq.heappop(heap) == 1
    assert heap[0] == 2
    assert hq.heappop(heap) == 2


def test_heappushpop():
    init_list = [2, 5, 1, 8, 3]
    heap = []
    [hq.heappush(heap, x) for x in init_list]

    assert hq.heappushpop(heap, 7) == 1
    assert len(heap) == 5


def test_heapify():
    heap = [2, 5, 1, 8, 3]
    hq.heapify(heap)
    assert heap[0] == 1


def test_heapreplace():
    init_list = [2, 5, 1, 8, 3]
    heap = []
    [hq.heappush(heap, x) for x in init_list]
    assert 1 == hq.heapreplace(heap, 4)  # remove 1 and add 4
    assert 2 == hq.heapreplace(heap, 0)  # remove 2 and add 0


def test_key():
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = hq.nsmallest(3, portfolio, key=lambda x: x['price'])
    exp = hq.nlargest(3, portfolio, key=lambda x: x['price'])
    print(cheap)
    print(exp)


def heapsort(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value)
    return [hq.heappop(h) for i in range(len(h))]


def test_sort():
    l = heapsort(([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    assert l == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
