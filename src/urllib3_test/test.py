import urllib3


def test1():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://httpbin.org/robots.txt')
    assert r.data == b'User-agent: *\nDisallow: /deny\n'
