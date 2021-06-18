class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):  # 如果找不到的键就是字符串，抛出 KeyError
            raise KeyError(key)
        return self[str(key)]  # 如果找不到的键不是字符串，转换成字符串继续查找

    def get(self, key, default=None):
        try:
            return self[key]  # 把查找工作用 self[key] 的形式委托给 __getitem__，这样在失败后还能通过 __missing__ 继续找
        except KeyError:
            return default

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()
