import sys


def test_version():
    print(sys.version)


def test_stderr():
    sys.stderr.write('This is an error message')
