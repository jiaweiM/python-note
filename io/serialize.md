# Serialization

- [Serialization](#serialization)
  - [pickle](#pickle)
    - [写入文件](#写入文件)
    - [从文件读取](#从文件读取)
    - [序列化为字节](#序列化为字节)
  - [json](#json)
  - [参考](#参考)

2021-06-30, 14:50
***

## pickle

`pickle` 模块是 Python 标准库，用于序列化对象。

`pickle` 可以保存所有基础类型以及自带的集合类型。

### 写入文件

例如，序列化包含多种类型的字典：

```py
entry = {}
entry['title'] = "Dive into history, 2009 edition"
entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['published'] = True

import time
entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')

import pickle
with open('entry.pickle', 'wb') as f:
    pickle.dump(entry, f)
```

### 从文件读取

从文件载入对象；

```py
with open('entry.pickle', 'rb') as f:
    entry = pickle.load(f)
    print(entry)
```

### 序列化为字节

```py
>>> b = pickle.dumps(entry) # 注意这儿用的函数是 `dupms`，带 `s`
>>> type(b)
<class 'bytes'>
>>> entry3 = pickle.loads(b)
>>> entry3 == entry
True
```

## json

`Pickle` 是 Python 特有的序列化格式，无法在其他编程语言中使用，而 JSON 是一种通用格式。

使用内置的 `json` 序列化为 json 格式：

```py
basic_entry = {}
basic_entry['id'] = 256
basic_entry['title'] = 'Dive into history, 2009 edition'
basic_entry['tags'] = ('diveintopython', 'docbook', 'html')
basic_entry['published'] = True
basic_entry['comments_link'] = None
import json
with open('basic.json', mode='w', encoding='utf-8') as f:
    json.dump(basic_entry, f)
```

另外，可以设置缩进，从而生成可读性更好的 JSON 文件:

```py
with open('basic.json', mode='w', encoding='utf-8') as f:
    json.dump(basic_entry, f, indent=2)
```

JSON 和 Python 3 类型映射：

|JSON|Python3|
|---|---|
|object|dict|
|array|list|
|string|string|
|integer|integer|
|real number|float|
|true|True|
|false|False|
|null|None|

需要注意的是，JSON 不支持 tuple 以及 `bytes` 类型。


## 参考

- Dive Into Python 3, Mark Pilgrim
