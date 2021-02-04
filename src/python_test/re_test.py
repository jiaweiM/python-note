import re


def test_re():
    assert not re.match("a", "cat")
    assert re.search("a", "cat")
    assert not re.search("c", "dog")
    assert 3 == len(re.split("[ab]", "carbs"))
    assert "R-D-" == re.sub("[0-9]", "-", "R2D2")
