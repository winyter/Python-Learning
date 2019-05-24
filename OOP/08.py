'''
多态：Mixin
'''


class Person():
    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleeping...")

#传统多继承写法
class Teacher(Person):
    def work(self):
        print("working...")

class Student(Person):
    def study(self):
        print("learning...")

    def say(self):
        print("saying...")

class Tutor(Teacher, Student):
    pass

t = Tutor()
#根据这个MRO可以看到，传统的多继承强调一级一级的继承，强调层级
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

print("*" * 20)

#Minxin下的多继承写法
class TeacherMixin():       #从这里可以看出，Teacher类不再去继承Person类，下面的Student类同理
    def work(self):
        print("working...")

class StudentMixin1():
    def study(self):
        print("learning...")

class StudentMixin2():          #对比上面可以看到，我把原来一个类中的两个方法剥离成了两个类，里面分别放入了一个方法，这种写法正是迎合了Mixin的设计模式：一个类只放一个功能，如果有多个功能，分成多个Mixing类进行存放
    def say(self):
        print("saying...")

class TutorMixin(Person, TeacherMixin, StudentMixin1,StudentMixin2):         #从这里看到，采用了Mixin写法后，Tutor类仅有一个真正意义上的父类Person，而其他的类，仅仅是作为扩展功能的功能类，一个功能对应一个功能类，实现了自由组合和模块化
    pass

tM = TutorMixin
print(TutorMixin.__mro__)       #可以看到，此时的MRO列表就显得扁平化了，所有类的顺序均按照括号内的顺序排列，而不需要一级一级的去查找父类
print(t.__dict__)
print(TutorMixin.__mro__)