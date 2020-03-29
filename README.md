# Python Study Notes

- [Python Study Notes](#python-study-notes)
  - [Python 基础](#python-%e5%9f%ba%e7%a1%80)
  - [集成模块](#%e9%9b%86%e6%88%90%e6%a8%a1%e5%9d%97)
  - [第三方库](#%e7%ac%ac%e4%b8%89%e6%96%b9%e5%ba%93)
  - [Unit Test](#unit-test)
  - [Tools](#tools)
  - [TensorFlow](#tensorflow)
  - [scikit-learn](#scikit-learn)
  - [PyTorch](#pytorch)
  - [Matplotlib](#matplotlib)
  - [Keras](#keras)
  - [NumPy](#numpy)
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
  - [参考](#%e5%8f%82%e8%80%83)
    - [代码练习](#%e4%bb%a3%e7%a0%81%e7%bb%83%e4%b9%a0)
    - [Python 教程](#python-%e6%95%99%e7%a8%8b)
  - [Data Analysis](#data-analysis)
    - [书籍](#%e4%b9%a6%e7%b1%8d)
      - [Intermediate Python](#intermediate-python)
    - [Fluent Python](#fluent-python)

***

## Python 基础

- [Python 简介](basic/0_intro.md)
- [语法](basic/1_syntax.md)
- [数据类型](basic/types.md)
- [string](basic/string.md)
- [函数](basic/function.md)
  - [函数总结](basic/func_api.md)
- [集合](basic/collect.md)
- [迭代器](basic/iterator.md)
- [生成器](basic/generator.md)
- [IO](basic/io.md)
- [类和对象](basic/class.md)
- [异常处理](basic/exception.md)

## 集成模块

- [pathlib](modules/pathlib.md)
- [itertool](api/itertool.md)
- [Numpy](numpy\contents.md)
- [pandas](pandas\intro.md)

## 第三方库

- [pandas](pandas/0_pandas_toc.md)

## Unit Test

- [pytest](tools/pytest.md)

## Tools

- [Visual Studio Code](py_vscode/0_vscode_toc.md)
- [pip](tools/pip.md)
- [pyCharm](tools/pycharm.md)
- [VS Code](tools/vscode_python.md)

## TensorFlow

“TensorFlow 是一个使用数据流图进行数值计算的开源软件库。图形节点表示数学运算，而图形边缘表示在它们之间流动的多维数据阵列（张量）。这种灵活的体系结构使用户可以将计算部署到桌面、服务器或移动设备中的一个或多个 CPU/GPU，而无需重写代码。 ”

GitHub 地址： https://github.com/tensorflow/tensorflow

## scikit-learn

scikit-learn 是一个基于 NumPy，SciPy 和 matplotlib 的机器学习 Python 模块。它为数据挖掘和数据分析提供了简单而有效的工具。SKLearn 所有人都可用，并可在各种环境中重复使用。

GitHub 地址： https://github.com/scikit-learn/scikit-learn

## PyTorch

PyTorch 是一个 Python 包，提供两个高级功能：

- 具有强大的 GPU 加速度的张量计算（如 NumPy）
- 基于磁带的自动编程系统构建的深度神经网络

你可以重复使用自己喜欢的 Python 软件包，如 NumPy，SciPy 和 Cython，以便在需要时扩展 PyTorch。”

GitHub 地址： https://github.com/pytorch/pytorch

## Matplotlib

Matplotlib 是一个 Python 2D 绘图库，可以生成各种出版品质的硬拷贝格式和跨平台交互式环境数据。Matplotlib 可用于 Python 脚本，Python 和 IPython shell（例如 MATLAB 或 Mathematica），Web 应用程序服务器和各种图形用户界面工具包。

GitHub 地址： https://github.com/matplotlib/matplotlib

## Keras

Keras 是一个高级神经网络 API，用 Python 编写，能够在 TensorFlow，CNTK 或 Theano 之上运行。它旨在实现快速实验，能够以最小的延迟把想法变成结果，这是进行研究的关键。

GitHub 地址： https://github.com/keras-team/keras

## [NumPy](numpy\01_content.md)

NumPy 是使用 Python 进行科学计算所需的基础包。它提供了强大的 N 维数组对象，复杂的（广播）功能，集成 C / C ++ 和 Fortran 代码的工具以及有用的线性代数，傅里叶变换和随机数功能。

其提供的多维数组比 Python 的嵌套 list 要快许多。

GitHub 地址： https://github.com/numpy/numpy

## SciPy

SciPy（发音为”Sigh Pie“）是数学、科学和工程方向的开源软件，包含统计、优化、集成、线性代数、傅立叶变换、信号和图像处理、ODE 求解器等模块。相对 NumPy 扩展了许多功能。

GitHub 地址： https://github.com/scipy/scipy

## Apache MXNet

Apache MXNet（孵化）是一个深度学习框架，旨在提高效率和灵活性，让你可以混合符号和命令式编程，以最大限度地提高效率和生产力。 MXNet 的核心是一个动态依赖调度程序，可以动态地自动并行化符号和命令操作。

GitHub 地址： https://github.com/apache/incubator-mxnet

## Theano

Theano 是一个 Python 库，让你可以有效地定义、优化和评估涉及多维数组的数学表达式。它可以使用 GPU 并实现有效的符号区分。

GitHub 地址：https://github.com/Theano/Theano

## Bokeh

Bokeh 是一个用于 Python 的交互式可视化库，可以在现代 Web 浏览器中实现美观且有意义的数据视觉呈现。使用 Bokeh，你可以快速轻松地创建交互式图表、仪表板和数据应用程序。

GitHub 地址： https://github.com/bokeh/bokeh

## XGBoost

XGBoost 是一个优化的分布式梯度增强库，旨在变得高效、强大、灵活和便携。它在 Gradient Boosting 框架下实现机器学习算法。XGBoost 提供了梯度提升决策树（也称为 GBDT，GBM），可以快速准确地解决许多数据科学问题，可以在主要的分布式环境（Hadoop，SGE，MPI）上运行相同的代码，并可以解决数十亿个示例之外的问题。

GitHub 地址：https://github.com/dmlc/xgboost

## Gensim

Gensim 是一个用于主题建模、文档索引和大型语料库相似性检索的 Python 库，目标受众是自然语言处理（NLP）和信息检索（IR）社区。

GitHub 地址： https://github.com/RaRe-Technologies/gensim

## Scrapy

Scrapy 是一种快速的高级 Web 爬行和 Web 抓取框架，用于抓取网站并从其页面中提取结构化数据。它可用于从数据挖掘到监控和自动化测试的各种用途。

GitHub 地址： https://github.com/scrapy/scrapy

## Caffe

Caffe 是一个以表达、速度和模块化为基础的深度学习框架，由伯克利人工智能研究（BAIR）/ 伯克利视觉与学习中心（BVLC）和社区贡献者开发。

GitHub 地址： https://github.com/BVLC/caffe

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

## 参考

[The Python Language Reference](https://docs.python.org/3.7/reference/index.html#reference-index)

[The Python Standard Library](https://docs.python.org/3.7/library/index.html#library-index)

[Python 文档](https://docs.python.org/3/)

[Dream in Code](https://www.dreamincode.net)  
教程及共享项目。

[Jupyter 例子](https://www.zhihu.com/question/37490497)

### 代码练习

[Practice Python](https://www.practicepython.org/)  
包含36个Python 入门练习题。

[Python Exercies, Practice, Solution](https://www.w3resource.com/python-exercises/)  
包含丰富的练习题。

### Python 教程

- [The Python Tutorial 官方教程](https://docs.python.org/3/tutorial/index.html)
- [Learn Python the hard way](https://learnpythonthehardway.org/book/)    
强烈推荐的入门教程，用一个个实例进行教学。
- [Python Wiki](https://wiki.python.org/moin/BeginnersGuide/Programmers)
- [x] [PyCharm使用简易教程](https://www.guru99.com/creating-your-first-python-program.html)

- [Teaching materials for the probabilistic graphical modesl and deep learning classes at Stanford](https://github.com/kuleshov/cs228-material)

- [Solo Learn](https://www.sololearn.com/Course/Python/)  
一步一步根据习题进行教学，很不错的入门教程。

- [Learn Python](https://www.learnpython.org/)

- [The Python Guru](https://thepythonguru.com/)  
比较简洁。
- [Zet Code](https://thepythonguru.com/)
- [W3C Python 教程](https://www.w3schools.com/python/)

- https://pythonprogramming.net/  
包含诸多Python 数据分析教程。

- https://www.python-course.eu/python3_course.php

- [A Byte of Python](https://python.swaroopch.com/)

- [Programiz Python 实例教程](https://www.programiz.com/python-programming)  
  包含丰富的实例，推荐。

- [x] [Dive Into Python 3](https://diveinto.org/python3/table-of-contents.html)

- [tutorials point](https://www.tutorialspoint.com/python/index.htm)

- [Google's Python Class](https://developers.google.com/edu/python/)

## Data Analysis

- [Scientific Python Lectures](https://github.com/jrjohansson/scientific-python-lectures)

### 书籍

- [Python Cookbook](https://python3-cookbook.readthedocs.io/zh_CN/latest/)

[书中源码](https://github.com/dabeaz/python-cookbook)

#### Intermediate Python

翻译：《Python 进阶》  
英文版地址：http://book.pythontips.com/en/latest/  
翻译本地址： https://eastlakeside.gitbooks.io/interpy-zh/content/

### Fluent Python

《流畅的Python》

[GitHub 地址](https://github.com/fluentpython)

这本书在某些方面可能过于简洁，但对于中级到高级开发人员来说，Fluent Python可能是绝对最好的编程书籍。一个开发者一旦你掌握了基础知识，就开始迷茫了，而Fluent Python用了将近800页的内容，来为你指明方向。

**优点和缺点**

这本书中的每一个主题都非常紧凑，而且非常详细，包括代码示例和解释。这对于能够理解的人来说简直如获至宝，对于不理解的人来说就是灾难了

优点:

- 非常详细的解释和代码示例
- 作者有着过硬的Python功底，20多年的工作经验，是一个值得信赖的老师
- 读者可以了解到几乎所有的高级Python主题

缺点：
- 叙述方式不是我读过的书中最清晰的
- 不同小节之间衔接不够自然

- [利用Python进行数据分析](https://seancheney.gitbook.io/python-for-data-analysis-2nd/di-01-zhang-zhun-bei-gong-zuo)

