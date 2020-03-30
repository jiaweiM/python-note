import collections


def test_append():
    d1 = collections.deque()
    # add elements to the right side
    d1.append(10)
    d1.append(10.1)
    d1.append("abc")
    print(d1)



def test_from_iterable():
    primeNumbers = (3, 5, 7, 11)
    primeDeque = collections.deque(primeNumbers)
    print(primeDeque)
    primeDeque.append(13)
    primeDeque.append(17)
    primeDeque.appendleft(2)
    print(primeDeque)


def test_fix_size():
    dq = collections.deque(maxlen=5)
    dq.append(10)
    dq.append(20)
    dq.append(30)
    dq.append(40)
    dq.append(50)
    print(dq)
    dq.append(60)
    print(dq)
    dq.appendleft(6)
    print(dq)
