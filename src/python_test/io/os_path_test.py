import os


def test_join():
    path = os.path.join("datasets", "housing")
    assert path == "datasets\housing"
