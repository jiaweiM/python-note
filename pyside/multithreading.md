# Qt 多线程技术

- [Qt 多线程技术](#qt-多线程技术)
  - [简介](#简介)
    - [QThread](#qthread)
    - [QThreadPool](#qthreadpool)
  - [参考](#参考)

2021-06-29, 11:17
***

## 简介

Qt 为多线程提供了许多类和函数。主要有以下四种不同的方法。

|特征|QThread|QThreadPool|QtConcurrent|WorkerScript|
|---|---|---|---|---|
|语言|C++|C++|C++|QML|
|指定线程优先级|✔️|✔️||||
|运行事件循环|✔️||||
|线程通过信号接收更新数据|

### QThread

`QThread` 是带有可选事件循环的底层 API，是 Qt 所有线程控制的基础。每个 `QThread` 代表一个线程。

`QThread` 可以直接实例化，也可以扩展该类：

- 直接实例化 `QThread` 提供了并行事件循环，从而允许在辅助线程中调用 `QObject` 插槽。
- 扩展 `QThread` 可以在启动事件循环之前初始化新线程，也可以在没有事件循环的情况下运行并行代码。

### QThreadPool

`QThreadPool` 和 `QRunnable` 用于复用线程。

频繁地创建和销毁线程开销加大，为了减少这种开销，可以在已有线程上运行新任务。`QThreadPool` 包含可复用 `QThread` 集合。




## 参考

- https://doc.qt.io/qt-6/threads-technologies.html
