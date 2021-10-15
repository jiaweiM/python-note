# Python 学习笔记

- [Python 学习笔记](#python-学习笔记)
  - [Python 教程](#python-教程)
    - [Python 打包和分发](#python-打包和分发)
  - [工具包](#工具包)
    - [函数编程](#函数编程)
  - [单元测试](#单元测试)
  - [开发工具](#开发工具)
  - [TensorFlow](#tensorflow)
  - [scikit-learn](#scikit-learn)
  - [PyTorch](#pytorch)
  - [Keras](#keras)
  - [SciPy](#scipy)
  - [Apache MXNet](#apache-mxnet)
  - [Theano](#theano)
  - [Bokeh](#bokeh)
  - [XGBoost](#xgboost)
  - [Gensim](#gensim)
  - [Scrapy](#scrapy)
  - [Caffe](#caffe)
  - [Django](#django)
  - [BeautifulSoup](#beautifulsoup)
  - [Panda3D](#panda3d)
  - [pygame](#pygame)
  - [信息源](#信息源)
    - [awesome list](#awesome-list)

***

## Python 教程

- [Python 简介](basic/0_intro.md)
- [语法](basic/1_syntax.md)
- [数据类型](basic/types.md)
- [表达式](basic/8_expression.md)
- [模块](basic/module.md)
  - [`__main__`](basic/main.md)
- [包](basic/package.md)
  - [安装包](basic/package_install.md)
- [集合](basic/collect.md)
  - [list](basic/3_collect_list.md)
  - [tuple](basic/4_collect_tuple.md)
  - [set](basic/5_collect_set.md)
  - [dict](basic/6_collect_dict.md)
  - [deque](basic/7_collect_deque.md)
  - [defaultdict](api/collections_defaultdict.md)
  - [OrderedDict](api/collections_ordereddict.md)
- [IO](io/python_io.md)
  - [pathlib](io/pathlib.md)
  - [os.path](io/os.path.md)
- [类和对象](basic/class.md)
  - [继承](basic/class_inherit.md)
- [异常处理](basic/exception.md)
- [Property](basic/property.md)
- [Python 命令](basic/commands.md)

### Python 打包和分发

- [构建和分发](tools/distribute.md)
- [打包Python项目](tools/packaging.md)
- [wheel](tools/wheel.md)
- [setuptools](tools/setuptools.md)

|工具|功能|
|---|---|
|[pip](tools/pip.md)|Python 包管理|
|[venv](tools/venv.md)|创建虚拟环境|

## 工具包

- [heapq](api/heapq.md)
- [Numpy](numpy/0_numpy_toc.md)
- [pandas](pandas/0_pandas_toc.md)

### 函数编程

- [itertool](api/itertool.md)
- [operator](api/module_operator.md)

## 单元测试

- [pytest](unit_test/pytest.md)

## 开发工具

- [Visual Studio Code](py_vscode/0_vscode_toc.md)
- [pip](tools/pip.md)
- [pyCharm](tools/pycharm.md)
- [VS Code](tools/vscode_python.md)

## TensorFlow

“TensorFlow 是一个使用数据流图进行数值计算的开源软件库。图形节点表示数学运算，而图形边缘表示在它们之间流动的多维数据阵列（张量）。这种灵活的体系结构使用户可以将计算部署到桌面、服务器或移动设备中的一个或多个 CPU/GPU，而无需重写代码。 ”

[GitHub 地址](https://github.com/tensorflow/tensorflow)

## scikit-learn

scikit-learn 是一个基于 NumPy，SciPy 和 matplotlib 的机器学习 Python 模块。它为数据挖掘和数据分析提供了简单而有效的工具。SKLearn 所有人都可用，并可在各种环境中重复使用。

[GitHub 地址](https://github.com/scikit-learn/scikit-learn)

## PyTorch

PyTorch 是一个 Python 包，提供两个高级功能：

- 具有强大的 GPU 加速度的张量计算（如 NumPy）
- 基于磁带的自动编程系统构建的深度神经网络

你可以重复使用自己喜欢的 Python 软件包，如 NumPy，SciPy 和 Cython，以便在需要时扩展 PyTorch。”

[GitHub 地址](https://github.com/pytorch/pytorch)

## Keras

Keras 是一个高级神经网络 API，用 Python 编写，能够在 TensorFlow，CNTK 或 Theano 之上运行。它旨在实现快速实验，能够以最小的延迟把想法变成结果，这是进行研究的关键。

[GitHub 地址](https://github.com/keras-team/keras)

## SciPy

SciPy（发音为”Sigh Pie“）是数学、科学和工程方向的开源软件，包含统计、优化、集成、线性代数、傅立叶变换、信号和图像处理、ODE 求解器等模块。相对 NumPy 扩展了许多功能。

[GitHub 地址](https://github.com/scipy/scipy)

## Apache MXNet

Apache MXNet（孵化）是一个深度学习框架，旨在提高效率和灵活性，让你可以混合符号和命令式编程，以最大限度地提高效率和生产力。 MXNet 的核心是一个动态依赖调度程序，可以动态地自动并行化符号和命令操作。

[GitHub 地址](https://github.com/apache/incubator-mxnet)

## Theano

Theano 是一个 Python 库，让你可以有效地定义、优化和评估涉及多维数组的数学表达式。它可以使用 GPU 并实现有效的符号区分。

[GitHub 地址](https://github.com/Theano/Theano)

## Bokeh

Bokeh 是一个用于 Python 的交互式可视化库，可以在现代 Web 浏览器中实现美观且有意义的数据视觉呈现。使用 Bokeh，你可以快速轻松地创建交互式图表、仪表板和数据应用程序。

[GitHub 地址](https://github.com/bokeh/bokeh)

## XGBoost

XGBoost 是一个优化的分布式梯度增强库，旨在变得高效、强大、灵活和便携。它在 Gradient Boosting 框架下实现机器学习算法。XGBoost 提供了梯度提升决策树（也称为 GBDT，GBM），可以快速准确地解决许多数据科学问题，可以在主要的分布式环境（Hadoop，SGE，MPI）上运行相同的代码，并可以解决数十亿个示例之外的问题。

[GitHub 地](https://github.com/dmlc/xgboost)

## Gensim

Gensim 是一个用于主题建模、文档索引和大型语料库相似性检索的 Python 库，目标受众是自然语言处理（NLP）和信息检索（IR）社区。

[GitHub 地址](https://github.com/RaRe-Technologies/gensim)

## Scrapy

Scrapy 是一种快速的高级 Web 爬行和 Web 抓取框架，用于抓取网站并从其页面中提取结构化数据。它可用于从数据挖掘到监控和自动化测试的各种用途。

[GitHub 地址](https://github.com/scrapy/scrapy)

## Caffe

Caffe 是一个以表达、速度和模块化为基础的深度学习框架，由伯克利人工智能研究（BAIR）/ 伯克利视觉与学习中心（BVLC）和社区贡献者开发。

[GitHub 地址](https://github.com/BVLC/caffe)

## Django

Python 中最常用的 web 框架。

web framework
CherryPy, Flask

## BeautifulSoup

从网页上抓取数据。

## Panda3D

3D 游戏开发。

## pygame

2D 游戏开发。

## 信息源

- [Python Weekly](https://www.pythonweekly.com/)
- [PyCoder's Weekly](https://pycoders.com/)

### awesome list

awesome list 是精选的资源列表。通常会随着时间的推移而增长，它不适合用来追更，但是可以作为进一步研究的良好起点。

- [awesome-python by vinta](https://github.com/vinta/awesome-python)

其中包含了大量有趣的项目列表，和分为 80 多个主题类别的标准库模块。

- [pycrumbs by kirang89](https://github.com/kirang89/pycrumbs)

这个集中在有趣和有价值的文章，分为 100 多个类别，专门讨论特定的 Python 特性、通用编程技术等。

- [pythonidae by svaksha](https://github.com/svaksha/pythonidae)

这个 awesome 列表专注于使用 Python 的特定科学和技术领域，如数学、生物、化学、Web 开发、物理、图像处理等。主页包含超过 20 个主要类别页面的列表。
