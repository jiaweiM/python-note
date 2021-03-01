from string import Template

import pytest


def test_ctr():
    template = Template("Hello $name!")
    s = template.substitute(name="World")
    assert s == 'Hello World!'


def test_substitute():
    s = Template("$who likes $what")
    t = s.substitute(who='tim', what='kung pao')
    assert t == "tim likes kung pao"


def test_dict():
    template = Template("$who likes $what")
    dct = {"who": "Lilei", "what": "apple"}
    t = template.substitute(dct)
    assert t == "Lilei likes apple"


def test_substitute_dict():
    d = dict(who='tim')
    with pytest.raises(ValueError):
        Template('Give $who $100').substitute(d)


def test_substitute_keyerror():
    with pytest.raises(KeyError):
        Template('$who likes $what').substitute(dict(who='tim'))
