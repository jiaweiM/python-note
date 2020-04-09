from pathlib import *


def test_sub_dir():
    p = Path('..')
    dir_lst = [x for x in p.iterdir() if x.is_dir()]
    assert PurePath('../io') in dir_lst


def test_purepath():
    p = PurePath('path', 'to', "hell")
    assert p == PurePath('path/to/hell')
    assert PurePath(Path('path'), 'to/hell') == PurePath('path/to/hell')


def test_compare():
    assert not (PurePosixPath('foo') == PurePosixPath('FOO'))
    assert PureWindowsPath('foo') == PureWindowsPath("FOO")
    assert PureWindowsPath("FOO") in {PureWindowsPath("foo")}
    assert PureWindowsPath("C:") < PureWindowsPath("d:")


def test_slash():
    assert PurePosixPath('/etc') / 'init.d' / 'apache2' == PurePosixPath('/etc/init.d/apache2')
    assert '/usr' / PurePath('bin') == PurePath('/usr/bin')
