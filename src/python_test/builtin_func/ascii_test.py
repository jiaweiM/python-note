def test_normal():
    normal_text = 'Python is interesting'
    assert ascii(normal_text) == "'Python is interesting'"

    other_text = 'Pythön is interesting'
    assert ascii(other_text) == r"'Pyth\xf6n is interesting'"

    print('Pyth\xf6n is interesting')
