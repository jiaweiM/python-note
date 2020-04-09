# Python IO

- [Python IO](#python-io)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [函数](#%e5%87%bd%e6%95%b0)
    - [os.walk](#oswalk)

## 简介

文件是磁盘上命名地址，用于存储相关信息，用于将数据永久存储在非易失性存储器中。随机存取存储器（random access memory, RAM）是易失性的，计算机关机后数据丢失，因此我们都是使用文件存储数据。

## 函数

| 函数                          | 功能                                             |
| ----------------------------- | ------------------------------------------------ |
| os.chdir(dir)                 | 修改当前工作目录为指定路径                       |
| os.getcwd()                   | 返回当前工作目录                                 |
| os.getcwdb()                  | 以二进制对象的形式返回当前工作目录               |
| os.mkdir(dir)                 | 创建一个新的文件夹                               |
| os.path.exists(a_path)        | 检查文件是否存在                                 |
| os.path.isfile(a_path)        | 检查路径下是否是文件                             |
| os.path.isdir(a_path)         | 检查路径下是否是目录                             |
| os.rename(old_name, new_name) | 重命名文件或目录                                 |
| os.rmdir(dir)                 | 移除文件或目录。如果目录包含文件，则移除目录失败 |
| os.rmtree(dir)                | 移除目录及其内的所有文件                         |

### os.walk

对目录下的所有文件夹，生成三项值的 tuple：dirpath, dirnames, filenames。

| 返回值    | 说明         |
| --------- | ------------ |
| dirpath   | 目录路径     |
| dirnames  | 子目录名称   |
| filenames | 所有的文件名 |

返回的名称仅仅包含名称，如果要获得完整路径：`os.path.join(dirpath, name)`
