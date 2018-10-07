"""
元类 - 描述类的类
通过继承type可以定义元类 通过元类可以改变一个类的行为
"""
from random import randint


class SingletonMeta(type):

    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance


class President(metaclass=SingletonMeta):

    def __init__(self, name):
        self.name = name
        self.salary = randint(100000, 999999)

    def __str__(self):
        return f'{self.name}: {self.salary}'


def main():
    president1 = President('奥巴马')
    president2 = President('特朗普')
    print(president1)
    print(president2)
    print(president1 == president2)


if __name__ == '__main__':
    main()
