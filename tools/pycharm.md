# pyCharm

- [pyCharm](#pycharm)
  - [以 pytest 运行测试](#以-pytest-运行测试)
  - [部署](#部署)
  - [问题汇总](#问题汇总)
    - [无 Latest verion 信息](#无-latest-verion-信息)

## 以 pytest 运行测试

按如下进行设置即可：

![](images/2019-09-05-14-11-52.png)

## 部署

打开设置 `File | Settings | Build, Execution, Deployment`

## 问题汇总

### 无 Latest verion 信息

一般是 PyPI 源的配置问题，比如使用了旧的 PyPI 源 https://pypi.python.org/simple ，而非新源 https://pypi.org/simple。
