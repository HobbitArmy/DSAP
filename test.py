"""
for test only

"""

class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / 1

    @staticmethod   # 静态调用
    # staticmethod不需要表示自身对象的self和自身类的cls参数
    def static_method():
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod    # 类方法
    # classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数
    def class_method(cls):
        return cls.averag(cls.X, cls.Y)


class Son(Foo):
    X = 3
    Y = 5

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / 2

p = Son()
print(p.static_method())
print(p.class_method())