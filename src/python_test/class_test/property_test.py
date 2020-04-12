import pytest


class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

    @temperature.deleter
    def temperature(self):
        raise AttributeError("Can't delete attribute")


def test_getter():
    c = Celsius(37)
    assert c.temperature == 37
    with pytest.raises(ValueError):
        c.temperature = -275
    with pytest.raises(AttributeError):
        del c.temperature
