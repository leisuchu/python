class Foo:
    name = "leisuchu"
    def test_foo(self):
        print(self.name)


f = Foo()
print(Foo.name)
#leisuchu
"""
如果没有对对象中同名的属性操作，则对象中的同名属性会跟着类属性变化
"""
Foo.name = 'nakura'
print(f.name)
#nakura

"""
一旦对对象中同名的属性操作，那么即便类属性变化，对象属性还是不变
"""
f.name = 'sakura'
Foo.name = 'nakura'
print(f.name)
#sakura

#显示对象的所有属性，不包括类属性
f.__dict__()


