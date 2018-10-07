"""
多重继承 / MRO / 循环引用
"""
import weakref


class Dept:

    def __init__(self, no, name, location):
        self.no = no
        self.name = name
        self.location = location
        self.manage = None


class Emp:

    def __init__(self, no, name, job):
        self.no = no
        self.name = name
        self.job = job
        self.dept = None


class A():

    def foo(self):
        print('foo in A')


class B(A):
    pass


class C(A):

    def foo(self):
        print('foo in C')


class D(B, C):
    pass


def main():
	dept = Dept(10, '研发部', '成都')
	emp = Emp(1001, '骆昊', 'Python开发工程师')
	dept.manager = weakref.ref(emp)
	emp.dept = dept
	del dept
	del emp
    d = D()
    d.foo()
    # MRO - Method Resolution Order
    # Python 2 - 深度优先搜索
    # Python 3 - 类似于广度优先搜索(C3算法)
    # D.__mro__
    print(D.mro())
    d.bar()


if __name__ == '__main__':
    main()
