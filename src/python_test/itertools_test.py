from itertools import zip_longest
from itertools import groupby
from operator import itemgetter


def test_len3():
    numbers = [1, 2, 3]
    letters = ['a', 'b', 'c']
    longest = range(5)
    zipped = zip_longest(numbers, letters, longest, fillvalue='?')
    l = list(zipped)
    assert len(l) == 5
    assert l[3] == ('?', '?', 3)


def test_groupby():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    rows.sort(key=itemgetter('date'))
    for date, item in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in item:
            print(' ', i)
