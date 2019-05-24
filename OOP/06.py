'''
继承的特征案例
'''

class Person():
    name = "Noname"
    _age = 18       #定义一个受保护的成员属性，子类中可以访问
    __score = 0     #定义一个私有成员，那么在子类中就无法访问

    def sleep(self):
        print("sleeping......")
    def work(self):
        print("make some money")

class Teacher(Person):
    #子类可以定义自己的成员
    teacher_id = '1111'
    name = "winyter"

    def make_test(self):
        print("attention")

    def doing(self):
        #第一种调用父类方法的写法：<父类名>.<方法名>
        Person.sleep(self)      #此处需要注意，由于父类中该方法有一个参数传入，所以此处也需要self来代表一个参数的传入
        #第二种调用父类方法的写法：super().<方法名>，super()代表得到父类
        super().work()
        self.make_test()

t = Teacher()

print('*' * 20)
#子类可以调用父类中的除私有外的成员
print(t._age)
#以下调用会有报错
#print(t.__score)

print('*' * 20)
#以下语句执行可以看到_age这个成员，不管是在子类Teacher中，还是在Teacher的对象t中，都是直接指向父类中该成员属性，调用的均是父类中_age的值
print(id(t._age))
print(id(Person._age))
print(id(Teacher._age))

print('*' * 20)
#当子类和父类有相同名词的成员时，调用该成员优先调用子类中的该成员
print(t.name)

print('*' * 20)
#子类可以扩充父类的方法
t.doing()
