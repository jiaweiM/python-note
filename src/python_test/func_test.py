def double(x):
    """this is where you put an optional docstring
    that explains what the function does.
    for example, this function multiplies its input by 2"""
    return x * 2


def apply_to_ono(f):
    """calls the function f with 1 as its argument"""
    return f(1)


x = apply_to_ono(double)
print(x)
y = apply_to_ono(lambda x: x + 4)
print(y)


def my_print(message="my default message"):
    print(message)


try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")


def exp(base, power):
    return base ** power


def two_to_the(power):
    return exp(2, power)
