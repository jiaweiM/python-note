import re


def test_re():
    assert not re.match("a", "cat")
    assert re.search("a", "cat")
    assert not re.search("c", "dog")
    assert 3 == len(re.split("[ab]", "carbs"))
    assert "R-D-" == re.sub("[0-9]", "-", "R2D2")


def test_search():
    pattern = '[a-z]+'
    string = '---2344-Hello--World!'
    result = re.search(pattern, string)
    print(result)


def test_findall():
    ptn = '\d+'
    string = '123 hello 68. Old 88'
    result = re.findall(ptn, string)
    print(result)


def test_search2():
    s = 'foo123bar'
    m = re.search('123', s)
    if m:
        print('Found')
    else:
        print("Not found")
