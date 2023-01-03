# NumPy IO

- [NumPy IO](#numpy-io)
  - [NumPy binary files (NPY, NPZ)](#numpy-binary-files-npy-npz)
  - [Text files](#text-files)
  - [Raw binary files](#raw-binary-files)
  - [String formatting](#string-formatting)
  - [Memory mapping files](#memory-mapping-files)
  - [Text formatting options](#text-formatting-options)
  - [API](#api)
    - [numpy.loadtxt](#numpyloadtxt)
  - [参考](#参考)

***

## NumPy binary files (NPY, NPZ)

## Text files

## Raw binary files

## String formatting

## Memory mapping files

## Text formatting options

## API

### numpy.loadtxt

```python
numpy.loadtxt(fname, 
        dtype=<class 'float'>, 
        comments='#', 
        delimiter=None, 
        converters=None, 
        skiprows=0, 
        usecols=None, 
        unpack=False, 
        ndmin=0, 
        encoding='bytes', 
        max_rows=None, *, 
        quotechar=None, 
        like=None)
```

从文本文件加载数据。

文本文件的每一行必须包含相同数量的值。



## 参考

- https://numpy.org/doc/stable/reference/routines.io.html
