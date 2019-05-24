'''
继承的成员查找顺序
构造函数
'''

class China():
    def __init__(self, level):
        print('china {0}'.format(level))

    level1 = '1'

class Jiangsu(China):
    def __init__(self):
        print('jiangsu')

    level2 = '2'

class Zhengjiang(Jiangsu):
    def __init__(self):
        print('zhengjiang')

    level3 = '3'

class Nanjing(Jiangsu):
    level4 = '3'

class Tianjin(China):
    level5 = '2'

print('*' * 20)
#实例化类之前，构造函数会被先行调用
z = Zhengjiang()

print('*' * 20)
#当子类中没有的成员,会调用父类中的该成员
print(z.level2)

print('*' * 20)
#当子类中没有构造函数时，会调用父类的构造函数
n = Nanjing()

print('*' * 20)
#如果子类没有构造函数，那么在调用成员时，需要按照父类的构造函数的参数，来构建参数
#下面的语句会报错：TypeError: __init__() missing 1 required positional argument: 'level'
#t = Tianjin()
t = Tianjin("level")

print('*' * 20)
#super()以及MRO
print(Zhengjiang.__mro__)

