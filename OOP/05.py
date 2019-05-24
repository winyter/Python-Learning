'''
继承
'''

#不管对于哪个类，都有一个共同的父类：object
class Person():
    name = "noname"
    age = 0

    def sleep(self):
        print("sleeping")

#子类继承父类的语法，即在定义子类时，在子类的名称括号中，加上父类名即可
class Teacher(Person):
    #子类可以定义自己的成员属性和成员方法
    def make_test(self):
        pass

#子类的对象可以直接调用父类的成员属性和成员方法
t = Teacher()
print(t.name)
print(t.age)
t.sleep()
print(Teacher.age)