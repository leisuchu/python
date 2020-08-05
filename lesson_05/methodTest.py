"""
修饰器
"""


class Foo:
    # 类方法
    @classmethod
    def method(cls, name):
        print(cls)


class Boo:
    # 静态方法
    @staticmethod
    def static_method():
        print('static')
