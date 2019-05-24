'''
运算类魔法函数
'''

class Student():
    def __init__(self, name):
        self._name = name

    def __gt__(self, obj):
        print("{0} 会比 {1} 大吗".format(self._name, obj._name))
        return self._name > obj._name

stu1 = Student("one")
stu2 = Student("two")
print(stu1 > stu2)