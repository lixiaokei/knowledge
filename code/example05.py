"""
装饰器 - 代理模式 - AOP(面向切面编程)

横切关注功(与正常业务逻辑无关的功能)能应该从正常的业务逻辑中剥离
在Python代码中可以使用装饰器来剥离横切关注功能
在Web项目中可以使用中间件(拦截过滤器)来实现横切关注功能
"""
from functools import wraps
from time import time


class RecordTime():

    def __init__(self, output):
        self.output = output

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            self.output('%s: %fs' % (func.__name__, time() - start))
            return result

        return wrapper


def record_time(output):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output('%s: %fs' % (func.__name__, time() - start))
            return result

        return wrapper

    return decorator


@record_time(print)
@RecordTime(print)
def foo():
    print('Hello, world!')


def main():
    print(foo.__name__)
    foo()
    foo.__wrapped__()



if __name__ == '__main__':
    main()
