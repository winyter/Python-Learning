'''
定义一个类，和对象，并使用
'''

# 定义一个空类
class Student():
    pass

# 定义一个对象
jas = Student()

# 定义一个类，用来描述学Python的学生
class PythonStudent():
    #定义一个成员属性，并赋值为None
    name = None
    age = 18
    course = "Python"

    # 定义一个方法，写作业
    def doHomeWork(self):
        print("im doing homework")
        return None

# 实例化一个对象
winyter = PythonStudent()
# 调用对象的属性
print(winyter.name)
print(winyter.age)
print(winyter.course)

# 调用对象的方法
winyter.doHomeWork()

print(PythonStudent.__dict__)
print(winyter.__dict__)
