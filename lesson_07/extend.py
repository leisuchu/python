"""
继承
"""


class Fo:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('eat' + self.name)


# 继承
class Bo(Fo): pass


bo = Bo('leisuchu');
bo.eat()


# 方法重写
class Ao(Fo):
    def __init__(self, age):
        self.age = age


# 避免方法重写
class Co(Fo):
    def __init__(self, name, age):
        self.age = age
        # Fo.__init__(self, name)
        super().__init__(name)


# -------------多继承------------
class M1(Fo):
    def __init__(self, m1, name):
        self.m1 = m1
        Fo.__init__(self, name)


class M2(Fo):
    def __init__(self, m2, name):
        self.m2 = m2
        Fo.__init__(self, name)


class J(M1, M2):
    def __init__(self, m1, m2, name):
        M1.__init__(self, m1, name)
        M2.__init__(self, m2, name)


print(J.__mro__)
# -------------多继承------------
