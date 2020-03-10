# pip

## 包管理

检查更新:

```cmd
pip list –outdated
```

升级包：

```cmd
pip install --upgrade packagename
```

卸载包：

```cmd
pip uninstall packagename
```

## install

语法：

```cmd
pip install [options] <requirement specifier> [package-index-options] ...
pip install [options] -r <requirements file> [package-index-options] ...
pip install [options] [-e] <vcs project url> ...
pip install [options] [-e] <local project path> ...
pip install [options] <archive url/path> ...
```

### 安装包

```cmd
pip install SomePackage            # 最新版
pip install SomePackage==1.0.4     # 指定版本
pip install 'SomePackage>=1.0.4'     # 最低版
```

`-U, --upgrade` 更新

## pip 镜像

国内的一些镜像：

- 豆瓣, [https://pypi.doubanio.com/simple/](https://pypi.doubanio.com/simple/)
- 阿里云, [https://mirrors.aliyun.com/pypi/simple/](https://mirrors.aliyun.com/pypi/simple/)
- 清华大学
  - [https://pypi.tuna.tsinghua.edu.cn/simple/](https://pypi.tuna.tsinghua.edu.cn/simple/)
  - [https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/](https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/)
- 中国科学技术大学, [http://pypi.mirrors.ustc.edu.cn/simple/](http://pypi.mirrors.ustc.edu.cn/simple/)
- 华中科学技术大学, [http://pypi.hustunique.com/](http://pypi.hustunique.com/)

### 临时使用镜像

```cmd
pip install some-package -i https://mirrors.aliyun.com/pypi/simple/
```

### 设置默认镜像

升级 pip 到最新版：

```cmd
pip install pip -U
```

配置默认镜像：

```cmd
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

## 参考

- [Reference Guide](https://pip.pypa.io/en/stable/reference/)
