'''
类和对象的成员分析
'''

class A():
    name = 'winyter'
    age = 18

    def aa(self):
        name = "winyter1"
        age = 20
        print(self.name)
        print(self.age)
    def aaAgain(s):
        print(s.name)
        print(s.age)
    def bb():
        print("这是一个绑定类的方法")
    def cc(self):
        print(__class__.name)
        print(__class__.age)
    def dd():
        print(__class__.name)
        print(__class__.age)

print('*' * 20)
print(A.name)
print(A.age)
print(id(A.name))
print(id(A.age))
print(A.__dict__)

print('*' * 20)
a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print(a.__dict__)

print('*' * 20)
a.name = "winter"
a.age = 20
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print(a.__dict__)

print('*' * 20)
a.aa()

print('*' * 20)
a.aaAgain()

print('*' * 20)
# 绑定类的方法，需要通过类来调用，对象无法调用
A.bb()

print('*' * 20)
c = A()
c.cc()
A.dd()