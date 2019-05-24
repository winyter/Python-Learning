'''
成员描述符
'''

class Person():

    #该函数是在成员的属性在读取的时候所执行的操作，由于需要读取，所以这个函数需要有return
    def ifget(self):
        return self._name * 2

    #该函数是在成员的属性在赋值的时候所执行的操作，由于需要复制，所以这个函数需要有赋值语句
    def ifset(self, name):
        self._name = name.upper()

    #该函数是在成员的属性在删除的时候所执行的操作，如果不允许删除该属性，可以在这个函数的函数体中填写pass
    def ifdel(self):
#        self._name = "None"
        pass
    name = property(ifget, ifset, ifdel, "操作name")

p = Person()
p.name = "wInTer"
print(p.name)

#以下例子证明了在property的删除函数中放入pass可以防止该属性被删除
del  p.name
print(p.name)
