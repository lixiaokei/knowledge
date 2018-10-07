"""
迭代器
"""
from random import randint


class RandomInt():

    def __init__(self, num, start=0, end=65535):
        self.num = num
        self.start = start
        self.end = end
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.num:
            self.counter += 1
            return randint(self.start, self.end)
        raise StopIteration()


def main():
    it = RandomInt(10, 1, 100)
    # for val in it:
    # 	print(val)
    print(next(it))
    print(next(it))


if __name__ == '__main__':
    main()
