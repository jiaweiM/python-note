# Beautiful Soup

- [Beautiful Soup](#beautiful-soup)
  - [快速入门](#快速入门)
  - [使用方法](#使用方法)
  - [对象类型](#对象类型)
    - [Tag](#tag)
      - [Name](#name)
      - [Attributes](#attributes)
      - [多值属性](#多值属性)
    - [NavigableString](#navigablestring)
    - [BeautifulSoup](#beautifulsoup)
    - [注释和其它特殊字符串](#注释和其它特殊字符串)
  - [浏览文档树](#浏览文档树)
    - [子节点](#子节点)
      - [通过tag名称访问](#通过tag名称访问)
      - [.contents 和 .children](#contents-和-children)
      - [.descendants](#descendants)
      - [.string](#string)
      - [.strings 和 stripped_strings](#strings-和-stripped_strings)
    - [父节点](#父节点)
      - [.parent](#parent)
      - [.parents](#parents)
    - [兄弟节点](#兄弟节点)
      - [`.next_sibling` 和 `.previous_sibling`](#next_sibling-和-previous_sibling)
      - [`.next_siblings` 和 `.previous_siblings`](#next_siblings-和-previous_siblings)
    - [前后移动](#前后移动)
  - [搜索文档树](#搜索文档树)
    - [过滤器类型](#过滤器类型)
      - [字符串过滤](#字符串过滤)
      - [正则表达式](#正则表达式)
      - [列表](#列表)
      - [True](#true)
      - [函数](#函数)
    - [find_all](#find_all)
      - [name](#name-1)
      - [关键字参数](#关键字参数)
      - [string](#string-1)
      - [limit](#limit)
      - [recursive](#recursive)
    - [find](#find)
  - [输出](#输出)
    - [get_text()](#get_text)
  - [解析器](#解析器)
  - [参考](#参考)

2021-06-02, 15:05
***

## 快速入门

下面的 HTML 代码将作为例子在下面反复使用。这是爱丽丝梦游仙境里的一段内容：

```py
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
```

使用 `BeautifulSoup` 解析这段代码得到 `BeautifulSoup` 对象，并能够按照标准缩进格式输出：

```py
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
```

```html
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ;
and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
```

- 浏览数据

```py
soup.title
# <title>The Dormouse's story</title>

soup.title.name
# u'title'

soup.title.string
# u'The Dormouse's story'

soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']
# u'title'

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a') # 找所有的 <a> 标签
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
```

- 找文档中所有 `<a>` 标签的链接

```py
for link in soup.find_all('a'):
    print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie
```

- 从文档中提取所有文字内容：

```py
print(soup.get_text())
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...
```

## 使用方法

将字符串或者文件句柄传入 `BeautifulSoup` 构成方法，获得文档对象：

```py
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"))

soup = BeautifulSoup("<html>data</html>")
```

BS4 在构造时首先将文档内容转换为  Unicode 编码，然后选择合适的解析器来解析文档内容，或使用指定解析器解析。

## 对象类型

BS4 将 HTML 文档转换为树形结构，每个节点对应一个 Python 对象，所有对象可以归纳为 4 种： `Tag` , `NavigableString` , `BeautifulSoup` , `Comment` 。

### Tag

`Tag` 和 XML 或 HTML 文档中的标签相同，例如：

```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
type(tag)
# <class 'bs4.element.Tag'>
```

`Tag` 有很多属性和方法，其中 name 和 attributes 属性最重要。

#### Name

每个 tag 都有名称，通过 `.name` 属性获取：

```python
tag.name
# u'b'
```

可以修改该名称：

```python
tag.name = "blockquote"
tag
# <blockquote class="boldest">Extremely bold</blockquote>
```

#### Attributes

一个 tag 可以有多个属性。例如 `<b class="boldest">` 有一个 "class" 属性，其值为 "boldest"。tag 属性的操作方法与字典相同：

```python
tag['class']
# u'boldest'
```

可以使用 `.attrs` 直接访问属性字典：

```python
tag.attrs
# {'id': 'boldest'}
```

可以添加、删除或修改 tag 属性。和字典操作一样：

```python
tag['id'] = 'verybold'
tag['another-attribute'] = 1
tag
# <b another-attribute="1" id="verybold"></b>

del tag['id']
del tag['another-attribute']
tag
# <b>bold</b>

tag['id']
# KeyError: 'id'
tag.get('id')
# None
```

#### 多值属性

HTML 中定义了许多多值属性。例如常见的 `class` 属性，一个 tag 可以有多个 CSS 的 class。还有 `rel` , `rev` , `accept-charset` , `headers` , `accesskey` 等。BS4 中对多值属性返回一个 list:

```python
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.p['class']
# ["body", "strikeout"]

css_soup = BeautifulSoup('<p class="body"></p>')
css_soup.p['class'] # 一个值也是返回 list
# ["body"]
```

如果某个属性看起来像多值属性，但是 HTML 没有该定义，此时 BS4 返回字符串：

```python
id_soup = BeautifulSoup('<p id="my id"></p>')
id_soup.p['id']
# 'my id'
```

将 tag 转换为字符串时，多值属性合并为一个值：

```python
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
rel_soup.a['rel']
# ['index']
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>
```

对 XML 格式，没有多值属性，全部为字符串：

```python
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
xml_soup.p['class']
# u'body strikeout'
```

### NavigableString

BS4 使用 `NavigableString` 表示 tag 中的字符串：

```python
tag.string
# u'Extremely bold'
type(tag.string)
# <class 'bs4.element.NavigableString'>
```

`NavigableString`和 Python Unicode 字符串类似，只是额外添加了一些功能，在遍历文档树中会详细解释。使用 `unicode` (Python 2) 或 `str` (Python 3)
可以将 `NavigableString` 转换为 Unicode 字符串：

```python
unicode_string = str(tag.string)
unicode_string
# 'Extremely bold'
type(unicode_string)
# <type 'str'>
```

不能原位编辑字符串，不过可以使用 `replace_with()` 替换：

```python
tag.string.replace_with("No longer bold")
tag
# <b class="boldest">No longer bold</b>
```

`NavigableString` 支持遍历文档树和搜索文档树中的大部分方法，不过由于字符串不能像 tag 一样包含其它内容，所以不支持 `.contents` , `.string` 属性以及 `find()` 方法等。

如果要在 BS4 外使用 `NavigableString` ，则最好使用 `unicde()` 将其转换为常规 Python 字符串。因为 `NagigableString` 包含对整个文档树的引用，占用大量内存。

### BeautifulSoup

`BeautifulSoup` 表示整个文档。大多数情况可以将其作为 `Tag` 对象使用，即它支持导航树和搜索树中的大部分方法。

也可以按照修改树中的方法对整个文档进行修改：

```python
doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(text="INSERT FOOTER HERE").replace_with(footer)
# 'INSERT FOOTER HERE'
print(doc)
# <?xml version="1.0" encoding="utf-8"?>
# <document><content/><footer>Here's the footer</footer></document>
```

不过 `BeautifulSoup` 毕竟不是真正的 HTML 或 XML tag，所以没有 name 和 attributes。不过 BS4 给了它一个特殊名称 "[doument]"：

```python
soup.name
# '[document]'
```

### 注释和其它特殊字符串

`Tag` , `NavigableString` , `BeautifulSoup` 涵盖了 HTML 或 XML 文档的所有内容。就剩下注释和一些特殊标记：

```python
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
type(comment)
# <class 'bs4.element.Comment'>
```

`Comment` 是特殊的 `NagigableString` 类型：

```python
comment
# 'Hey, buddy. Want to buy a used parser'
```

当它作为 HTML 文档的一部分显示时，则以 HTML 注释格式显示：

```python
print(soup.b.prettify())
# <b>
#  <!--Hey, buddy. Want to buy a used parser?-->
# </b>
```

BS4 还为嵌入式样式表（ `<style>` 标签内容）定义了 `Stylesheet` 类, 为嵌入式 JavaScript （ `<script>` 标签内容）定义 `Script` 类，为 HTML 模板定义了 `TemplateString` 类。这些类的使用和 `NavigableString` 完全一样。

对 XML 文档中的特定内容也定义了具体类： `CData` , `ProcessingInstruction` , `Declaration` , `Doctype` 。和 `Comment` 一样，这些类也是 `NavigableString` 的子类。

## 浏览文档树

实例 HTML 文档：

```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

### 子节点

每个 tag 可以包含字符串和其它 tag，这些都是 tag 的子节点。BS4 提供了许多操作和遍历子节点的**属性**。
> BS4 字符串不支持这些属性，因为字符串没有子节点。

#### 通过tag名称访问

使用 tag 名称是访问文档树的最简单方式，例如要访问 `<head>` 标签，可以直接使用 `soup.head` ：

```python
soup.head
# <head><title>The Dormouse's story</title></head>

soup.title
# <title>The Dormouse's story</title>
```

可以反复使用该方法访问文档内容。例如，方位 `<body>` 标签下的第一个 `<b>` 标签：

```python
soup.body.b
# <b>The Dormouse's story</b>
```

使用 tag 名称访问，只返回第一个匹配的 tag：

```python
soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
```

如果要获得所有的 `<a>` tag，则需要使用搜索文档树中那些更复杂的方法，例如 `find_all()` ：

```python
soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

#### .contents 和 .children

`.contents` 包含 tag 所有子节点列表：

```python
head_tag = soup.head
head_tag
# <head><title>The Dormouse's story</title></head>

head_tag.contents
# [<title>The Dormouse's story</title>]

title_tag = head_tag.contents[0]
title_tag
# <title>The Dormouse's story</title>
title_tag.contents
# ['The Dormouse's story']
```

`BeautifulSoup` 对象包含唯一子节点 `<html>` ：

```python
len(soup.contents)
# 1
soup.contents[0].name
# 'html'
```

字符串没有子节点，所以也没有 `.contents` 属性：

```python
text = title_tag.contents[0]
text.contents
# AttributeError: 'NavigableString' object has no attribute 'contents'
```

`.children` 以生成器的方式返回所有子元素：

```python
for child in title_tag.children:
    print(child)
# The Dormouse's story
```

#### .descendants

`.contents` 和 `.children` 属性只返回 tag 的直接子节点。例如， `<head>` 标签的直接子节点只有 `<title>` :

```python
head_tag.contents
# [<title>The Dormouse's story</title>]
```

但是 `<title>` tag 也有一个子节点，即字符串内容。从某种意义上来说，该字符串也是 `<head>` 的子节点。 `.descendants` 属性可以遍历 tag 的所有子元素，包括非直接子元素：

```python
for child in head_tag.descendants:
    print(child)
# <title>The Dormouse's story</title>
# The Dormouse's story
```

#### .string

如果一个 tag 只有一个 `NavigableString` 子节点，则可以直接使用 `.string` 访问：

```python
title_tag.string
# 'The Dormouse's story'
```

如果一个 tag 只包含另一个 tag，而子 tag 包含 `.string` 属性，则在父节点上调用 `.string` 和子节点上调用 `.string` 一样：

```python
head_tag.contents
# [<title>The Dormouse's story</title>]

head_tag.string
# 'The Dormouse's story'
```

如果一个 tag 包含多个子节点，则无法确定 `.string` 内容，此时返回 `None` ：

```python
print(soup.html.string)
# None
```

#### .strings 和 stripped_strings

如果一个 tag 有多个子节点，则可以使用 `.strings` 生成器查看所有字符串：

```python
for string in soup.strings:
    print(repr(string))
    '\n'
# "The Dormouse's story"
# '\n'
# '\n'
# "The Dormouse's story"
# '\n'
# 'Once upon a time there were three little sisters; and their names were\n'
# 'Elsie'
# ',\n'
# 'Lacie'
# ' and\n'
# 'Tillie'
# ';\nand they lived at the bottom of a well.'
# '\n'
# '...'
# '\n'
```

字符串往往有许多额外的空格，使用 `.stripped_strings` 生成器可以删除这些空格：

```python
for string in soup.stripped_strings:
    print(repr(string))
# "The Dormouse's story"
# "The Dormouse's story"
# 'Once upon a time there were three little sisters; and their names were'
# 'Elsie'
# ','
# 'Lacie'
# 'and'
# 'Tillie'
# ';\n and they lived at the bottom of a well.'
# '...'
```

单纯的空格字符串、已经字符串开头和结尾的空格都被删除。

### 父节点

每个 tag 和字符串都有父节点。

#### .parent

使用 `.parent` 属性访问父节点。继续上面的例子， `<head>` 是 `<title>` 的父节点：

```python
title_tag = soup.title
title_tag
# <title>The Dormouse's story</title>
title_tag.parent
# <head><title>The Dormouse's story</title></head>
```

title 字符串的父节点为 `<Title>` ：

```python
title_tag.string.parent
# <title>The Dormouse's story</title>
```

顶级标签 `<html>` 的父节点为 `BeautifulSoup` 对象：

```python
html_tag = soup.html
type(html_tag.parent)
# <class 'bs4.BeautifulSoup'>
```

`BeautifulSoup`的父节点为 `None` ：

```python
print(soup.parent)
# None
```

#### .parents

`.parents` 属性遍历所有父节点。例如，从 `<a>` tag 开始向上遍历到文档的顶部：

```python
link = soup.a
link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
for parent in link.parents:
    print(parent.name)
# p
# body
# html
# [document]
```

### 兄弟节点

看一个简单文件：

```python
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'html.parser')
print(sibling_soup.prettify())
#   <a>
#    <b>
#     text1
#    </b>
#    <c>
#     text2
#    </c>
#   </a>
```

`<b>` tag 和 `<c>` tag 在同一层，它们是同一个 tag 的子节点。这类节点称为兄弟节点。

#### `.next_sibling` 和 `.previous_sibling`

可以使用 `.next_sibling` 和 `.previous_sibling` 查看同一层的节点：

```python
sibling_soup.b.next_sibling
# <c>text2</c>

sibling_soup.c.previous_sibling
# <b>text1</b>
```

`<b>` tag 有 `.next_sibling` ，但是没有 `.previous_sibling`；<c> 有 `.previous_sibling` 但是没有 `.next_sibling` ，此时返回 `None` ：

```python
print(sibling_soup.b.previous_sibling)
# None
print(sibling_soup.c.next_sibling)
# None
```

字符串 "text1" 和 "text2" 不是兄弟节点，因为它们的父节点不同：

```python
sibling_soup.b.string
# 'text1'

print(sibling_soup.b.string.next_sibling)
# None
```

在实际 HTML 文件中，tag 的 `.next_sibling` 和 `.previous_sibling` 通常是包含空格的字符串。回到爱丽丝：

```python
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
```

你可能认为第一个 `<a>` tag 的 `.next_sibling` 是第二个 `<a>` tag。但实际上是分隔第一个 `<a>` 和第二个 `<a>` 的逗号和换行符：

```python
link = soup.a
link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

link.next_sibling
# ',\n '
```

第二个 `<a>` 其实是逗号的 `.next_sibling` ：

```python
link.next_sibling.next_sibling
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
```

#### `.next_siblings` 和 `.previous_siblings`

所有兄弟节点的生成器：

```python
for sibling in soup.a.next_siblings:
    print(repr(sibling))
# ',\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# ' and\n'
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# '; and they lived at the bottom of a well.'

for sibling in soup.find(id="link3").previous_siblings:
    print(repr(sibling))
# ' and\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# ',\n'
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# 'Once upon a time there were three little sisters; and their names were\n'
```

### 前后移动

## 搜索文档树

BS4 定义了许多搜索的方法，功能都相似，其中 `find()` 和 `find_all()` 最常用。依然以爱丽丝为例：

```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

通过过滤器可以筛选感兴趣内容。

### 过滤器类型

在讨论 `find_all()` 等搜索方法之前，我们先看看传递给这些方法过滤器类型。使用这些过滤器，可以根据 tag 名称、属性、文本等信息过滤。

#### 字符串过滤

字符串是最简单的过滤器。将字符串传递给搜索方法，BS4 将对字符串进行匹配。例如查找所有的 `<b>` tag：

```python
soup.find_all('b')
# [<b>The Dormouse's story</b>]
```

如果传入 byte 字符串，BS4 默认其编码为 UTF-8。

#### 正则表达式

对正则表达式，BS4 使用其 `search()` 方法匹配正则表达式。例如，查找所有以 "b" 开头的 tag：

```python
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b
```

查找所有包含字母 't' 的 tag:

```python
for tag in soup.find_all(re.compile("t")):
    print(tag.name)
# html
# title
```

#### 列表

如果使用列表过滤，BS4 匹配列表中的任意一项。例如查找所有的 `<a>` 和 `<b>` tag：

```python
soup.find_all(["a", "b"])
# [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

#### True

`True` 匹配任意值。此时匹配所有的 tags，但是不匹配字符串：

```python
for tag in soup.find_all(True):
    print(tag.name)
# html
# head
# title
# body
# p
# b
# p
# a
# a
# a
# p
```

#### 函数

如果以上的过滤器都无法满足你的额要求，此时可以使用函数过滤器。定义函数参数为元素类型，返回 `true` 表示通过功率，否则返回 `False` 。例如，查找包含 "class" 属性但是没有 "id" 属性的 tag:

```python
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
```

将该函数传递给 `find_all()` 函数，找到所有 <p> tag：

```python
soup.find_all(has_class_but_no_id)
# [<p class="title"><b>The Dormouse's story</b></p>,
#  <p class="story">Once upon a time there were…bottom of a well.</p>,
#  <p class="story">...</p>]
```

如果根据指定属性过滤，如 `href` 属性，此时传递给函数的参数是属性值，而不是整个 tag。例如，查找所有 `href` 属性和正则表达式不匹配的 `<a>` tag:

```python
import re
def not_lacie(href):
    return href and not re.compile("lacie").search(href)

soup.find_all(href=not_lacie)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

使用函数可以定义任意负责的过滤器。下面查找被字符串包围的 tag：

```python
from bs4 import NavigableString
def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
    print(tag.name)
# body
# p
# a
# a
# a
# p
```

### find_all

```python
find_all( name , attrs , recursive=True, string , **kwargs )
```

`find_all()` 搜索当前 tag 的所有子节点，根据过滤器获得匹配的所有子节点：

```python
soup.find_all("title")
# [<title>The Dormouse's story</title>]

soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]

soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

import re
soup.find(string=re.compile("sisters"))
# 'Once upon a time there were three little sisters; and their names were\n'
```

#### name

传入 `name` 值表示仅查找匹配该名称的 tags，其他 tags 和文本字符串均忽略：

```python
soup.find_all("title")
# [<title>The Dormouse's story</title>]
```

`name` 可以是字符串、正则表达式、列表、函数以及 True 过滤器。

#### 关键字参数

任何不能识别的参数都被转换为基于元素属性的过滤器。如果传入名为 `id` 的参数，BS4 将根据每个元素的 'id' 属性进行过滤：

```python
soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```

如果使用 `href` 参数，则 BS4对所有 tag 的 'href' 属性进行过滤：

```python
soup.find_all(href=re.compile("elsie"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
```

可以使用字符串、正则表达式、列表、函数或 True 过滤器对属性进行过滤。例如，查找所有包含 `id` 属性的 tags:

```python
soup.find_all(id=True)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

传入多个关键字参数，可以通过对多个属性进行过滤：

```python
soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
```

有些属性，如 HTML5 中的 `data-*` 属性不能作为参数名称：

```python
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'html.parser')
data_soup.find_all(data-foo="value")
# SyntaxError: keyword can't be an expression
```

此时可以将它们放入字典，并将字典作为 `attrs` 参数传入 `find_all()` 方法：

```python
data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]
```

另外，无法使用关键字参数检索 'name' 元素，因为 BS4 使用 `name` 参数指定标签名称本身。依然是可以将其传入 `attrs` 参数：

```python
name_soup = BeautifulSoup('<input name="email"/>', 'html.parser')
name_soup.find_all(name="email")
# []
name_soup.find_all(attrs={"name": "email"})
# [<input name="email"/>]
```

从某种程度上来说，关键字参数是多余的，例如下面两行是等价的：

```python
bs.find_all(id='text')
bs.find_all('', {'id':'text'})
```

而且使用上有限值，比如 `class` 属性和 `name` 属性就无法使用关键字参数。

#### string

通过 `string` 可以搜索字符串而不是标签。与 `name` 及关键字参数一样， `string` 也可以使用字符串、正则表达式、列表、函数以及 True 作为过滤器。例如：

```python
soup.find_all(string="Elsie")
# ['Elsie']

soup.find_all(string=["Tillie", "Elsie", "Lacie"])
# ['Elsie', 'Lacie', 'Tillie']

soup.find_all(string=re.compile("Dormouse"))
# ["The Dormouse's story", "The Dormouse's story"]

def is_the_only_string_within_a_tag(s):
    """Return True if this string is the only child of its parent tag."""
    return (s == s.parent.string)

soup.find_all(string=is_the_only_string_within_a_tag)
# ["The Dormouse's story", "The Dormouse's story", 'Elsie', 'Lacie', 'Tillie', '...']
```

虽然 `string` 是用来查找字符串的，但是可以和查找 tag 的参数合并使用。BS4 会查找所有 `.string` 满足 `string` 的tags。例如，查找所有 `.string` 为 "Elsie" 的 `<a>` 标签：

```python
soup.find_all("a", string="Elsie")
# [<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>]
```

`string` 参数是 BS 4.4.0 新加入的，在早起版本中称为 `text` ：

```python
soup.find_all("a", text="Elsie")
# [<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>]
```

#### limit

`find_all()` 函数返回匹配过滤器的所有 tag 和字符串，如果文档很大，就可能很耗时。如果你不需要所有结果，可以传入一个参数 `limit` 限制返回结果的个数。这和 SQL 中的 LIMIT 关键字效果一样。BS4 找到足够的结果时就停止收集。

在爱丽丝里有三个链接，我们可以只找前两个：

```python
soup.find_all("a", limit=2)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

```

#### recursive

如果调用 `mytag.find_all()` ，BS4 会检查 `mytag` 的所有子节点，子节点的子节点。如果你只想看 `mytag` 的子节点，此时可以设置 `recursive=False` 。

```python
soup.html.find_all("title")
# [<title>The Dormouse's story</title>]

soup.html.find_all("title", recursive=False)
# []
```

文档内容如下：

```html
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
...
```

<title> 标签在 <html> 标签内，但不是 <html> 的直接子节点，所以设置 `recursive=False` 时就无法匹配到 <title>。

BS4 提供了许多搜索方法，大部分方法的参数和 `find_all()` 相同，即 `name ` , `attrs` , `string` , `limit` 以及关键字参数。不过 `recursive` 参数仅 `find_all` 和 `find` 方法有。

### find

```python
find(name, attrs, recursive, string, **kwargs)
```

`find_all()` 方法扫描整个文档查找结果，但有时你只想要第一个结果。如果你知道文件里只有一个 <body> 标签，此时扫描整个文档就是浪费时间。除了在 `find_all` 中使用 `limit=1` 参数，直接使用 `find()` 方法更简洁：

```python
soup.find_all('title', limit=1)
# [<title>The Dormouse's story</title>]

soup.find('title')
# <title>The Dormouse's story</title>
```

两者唯一的区别是 `find_all()` 返回包含一个结果的列表， `find()` 直接返回结果。

`find_all()` 找不到匹配 tag 时返回空 list，而 `find()` 返回 `None` ：

```python
soup.head.title
# <title>The Dormouse's story</title>

soup.find("head").find("title")
# <title>The Dormouse's story</title>
```

## 输出

### get_text()

`get_text()` 方法返回文档或标签中的文本，以 Unicode 字符串的形式返回文档或 tag 下的所有文本：

```python
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup, 'html.parser')

soup.get_text()
'\nI linked to example.com\n'
soup.i.get_text()
'example.com'
```

可以指定一个分隔符，将所有文本串起来：

```python
soup.get_text("|")
'\nI linked to |example.com|\n'
```

也可以去除前后的空格：

```python
soup.get_text("|", strip=True)
'I linked to|example.com'
```

不过此时使用 `.stripped_strings` 生成器可能更好：

```python
[text for text in soup.stripped_strings]
# ['I linked to', 'example.com']
```

## 解析器

BS4 支持的主要解析器如下：

| **解析器** | **使用方法** | **优势** | **劣势** |
| :--- | :--- | :--- | :--- |
| Python标准库 | `BeautifulSoup(markup, "html.parser")` | 
- Python的内置标准库
- 执行速度适中
- 文档容错能力强
 | 
- Python 2.7.3 or 3.2.2)前的版本中文档容错能力差
 |
| lxml HTML 解析器 | `BeautifulSoup(markup, "lxml")` | 
- 速度快
- 文档容错能力强
 | 
- 需要安装C语言库
 |
| lxml XML 解析器 | `BeautifulSoup(markup, ["lxml-xml"])`
`BeautifulSoup(markup, "xml")` | 
- 速度快
- 唯一支持XML的解析器
 | 
- 需要安装C语言库
 |
| html5lib | `BeautifulSoup(markup, "html5lib")` | 
- 最好的容错性
- 以浏览器的方式解析文档
- 生成HTML5格式的文档
 | 
- 速度慢
- 不依赖外部扩展
 |

推荐使用 lxml 作为解析器，它效率更高. 在 Python 2.7.3 之前的版本和 Python3 中 3.2.2 之前的版本，必须安装lxml或html5lib, 因为那些Python版本的标准库中内置的HTML解析方法不够稳定.

## 参考

- [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Web Scraping  with Python, COLLECTING MORE DATA FROM THE MODERN WEB, 2ed
