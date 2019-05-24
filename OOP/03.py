'''
鸭子模型演示
'''

class A():
    name = "aaa"
    age = 1

    def __init__(self):
        self.name = "init"
        self.age = 0

    def aa(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbb"
    age = 2

print('*' * 20)
#这是基础的通过定义A类的一个对象a，来调用aa()方法，此处，self代理的就是a对象，而__init__可以理解是构造函数，有构造函数的类中，没有定义相应成员的方法在使用该成员时，会去构造函数中查找使用同名的成员，而不会如之前所说的那样，去类的实例中获取这个成员
a = A()
a.aa()

print('*' * 20)
#这是调用类A的方法，并传入对象a的形式来实现调用方法aa()，这个方式实际上和上面的方法没有区别，只是写法不同而已
A.aa(a)

print('*' * 20)
#这就是通过调用类A的方法，并传入类A的实例对象A来实现调用方法aa()，此处，self代理的就是类A的实例对象A，所以，本段代码的运行结果也可以看到，就是A的成员值
#但是需要注意，在使用类的实例对象时，就不可以使用定义的对象来调用类的方法，例如：a.aa(A) 的写法，程序会报错，简单的记法：调用类的成员，只能通过类来调用方法，对象比类小一级，调不动
A.aa(A)

print('*' * 20)
#此处展示了调用其他类的成员，这在Python中也是可行的，其结果就是类B中的成员值
A.aa(B)