'''
抽象类
'''

import abc

#声明一个类，并指定当前类的元类
class Person(metaclass=abc.ABCMeta):

    #定义一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass

    #定义类抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass

    #定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

