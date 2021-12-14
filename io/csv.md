# csv

## 简介

CSV 文件电子表格和数据库最常用的导入和导出格式。在 RFC 4180 尝试以标准化方式描述该格式之前，CSV 格式已经被使用很多年。由于缺乏定义良好的标准，不同应用程序产生的和使用的数据往往存在细微差异。这些差异使得处理来自多个源的 CSV 文件非常麻烦。尽管分隔符和引号字符不同，单总体格式非常相似，因此可以编写一个模块来高效操作这些数据，对程序员隐藏读取和写入数据的细节。

`csv` 模块实现了 CSV 读写功能：

- `reader` 和 `writer` 类读写序列数据；
- `DictReader` 和 `DictWriter` 以字典形式读写数据。

## reader

```py
csv.reader(csvfile, dialect='excel', **fmtparams)
```



## writer

## 参考

- https://docs.python.org/3/library/csv.html
