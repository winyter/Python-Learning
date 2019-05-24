'''
类的三种方法
'''

class Person():

    #实例方法，需要实例才能调用
    def eat(self):
        print(self)
        print("eating...")

    #类方法
    @classmethod
    def play(cls):
        print(cls)
        print("playing...")

    #静态方法
    #不需要第一个参数来代表自己或者类
    @staticmethod
    def say():
        print("saying...")

per = Person()

#实例方法调用
per.eat()

#类方法调用,类方法可以通过对象调用
Person.play()
per.play()

#静态方法，静态方法也可以通过对象调用
Person.say()
per.say()