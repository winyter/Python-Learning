'''
封装
'''

class Person():
    name = "winyter"
    __age = 18

p = Person()
print(p.name)
#下面的语句会报错，需要注意报错信息：
#'Person' object has no attribute '__age'：没有这个成员，也就是说，Python将这个变量保护起来了
#print(p.__age)
#name mangling改名策略，及其使用
print(Person.__dict__)      #该语句执行后，可以看到：'_Person__age': 18，证明了改名策略的固定格式
print(p._Person__age)
p._Person__age = 19
print(p._Person__age)