import random


def test_random():
    """
    random() produces numbers uniformly between 0 and 1
    """
    four_uniform_randoms = [random.random() for _ in range(4)]


def test_seed():
    random.seed(10)
    print(random.random())
    random.seed(10)
    print(random.random())


def test_randrange():
    x = random.randrange(10)
    print(x)


def test_choice():
    a_list = ['apple', 'banana', 'cherry']
    print(random.choice(a_list))
