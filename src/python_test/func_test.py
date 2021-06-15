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


def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


def test_map_listgen():
    fact = factorial
    l = list(map(fact, range(6)))
    assert l == [1, 1, 2, 6, 24, 120]

    l2 = [fact(n) for n in range(6)]
    assert l2 == [1, 1, 2, 6, 24, 120]

    l = list(map(factorial, filter(lambda n: n % 2, range(6))))
    assert l == [1, 6, 120]
    l2 = [factorial(n) for n in range(6) if n % 2]
    assert l2 == [1, 6, 120]


def tag(name, *content, cls=None, **attrs):
    """生成一个或多个 HTML 标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


def test_tag():
    assert tag('br') == "<br />"  # 单个标签

    s = tag('p', 'hello')  # 单个内容
    assert s == "<p>hello</p>"

    s = tag('p', 'hello', 'world')  # 多个内容
    assert s == "<p>hello</p>\n<p>world</p>"

    s = tag('p', 'hello', id=33)  # 标签+内容+属性
    assert s == '<p id="33">hello</p>'

    s = tag('p', 'hello', 'world', cls='sidebar')  # 标签+内容*2+cls
    assert s == '<p class="sidebar">hello</p>\n<p class="sidebar">world</p>'

    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'cls': 'framed'}
    s = tag(**my_tag)  # 在 my_tag 前面加上 **，字典中的所有元素作为单个参数传入，同名键会绑定到对应的具名参数上，余下的则被 **attrs 捕获
    assert s == '<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'


def clip(text, max_len=80):
    """
    在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()


def test_info():
    assert clip.__defaults__ == (80,)
    print(clip.__code__)


from inspect import signature


def test_info2():
    sig = signature(clip)
    