"""
排序算法
衡量一个算法的好坏有两个指标：渐近时间复杂度和渐近空间复杂度
第一类：简单排序算法 - 简单选择排序、简单插入排序、冒泡排序 - O(n ** 2)
第二类：高级排序算法 - 快速排序、归并排序 - O(n * log2 n)

冒泡排序
68, 34, 12, 95, 73, 80, 57
34, 12, 68, 73, 80, 57, 95
12, 34, 68, 73, 57, 80
12, 34, 68, 57, 73
12, 34, 57, 68
12, 34, 57
12, 34

归并排序
68, 34, 12, 95, 73, 80, 57
[69, 34, 12], [95, 73, 80, 57]
[69], [34, 12], [95, 73], [80, 57]
[69], [34], [12], [95], [73], [80], [57]
----------------------------------------
[34, 69], [12, 95], [73, 80], [57]
[12, 34, 69, 95], [57, 73, 80]
[12, 34, 57, 69, 73, 80, 95]

快速排序
68, 34, 12, 95, 73, 80, 57
{34, 12, 57}，{68}，{95, 73, 80}
{12}, {34}, {57}，{68}, {73, 80}, {95}
{12}, {34}, {57}, {68}, {73}, {80}, {95}
"""
from collections import namedtuple


def fib1(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


# 爬楼梯 一次可以爬1个、2个、3个台阶
# 爬完10个台阶一共有多少种走法
def walk(num, result={}):
    if num == 0:
        return 1
    elif num < 0:
        return 0
    try:
        return result[num]
    except KeyError:
        result[num] = walk(num - 1) + walk(num - 2) + walk(num - 3)
        return result[num]


# 1 1 2 3 5 8 13 21 34 55 ...
# 动态规划 - 求解的问题有局部最优解或者最优子结构
def fib2(num, result={}):
    if num in (1, 2):
        return 1
    try:
        return result[num]
    except KeyError:
        result[num] = fib2(num - 1) + fib2(num - 2)
        return result[num]


def factorial(num):
    if num in (0, 1):
        return 1
    return num * factorial(num - 1)


# 分治法 - 将规模较大的问题划分为规模较小的子问题 用子问题解合并出原问题的解
# divide-and-conquer
def merge_sort(unsorted_items, *, comp=lambda x, y: x < y):
    if len(unsorted_items) <= 1:
        return unsorted_items[:]
    mid = len(unsorted_items) // 2
    left = merge_sort(unsorted_items[:mid], comp=comp)
    right = merge_sort(unsorted_items[mid:], comp=comp)
    return merge(left, right, comp=comp)


def merge(list1, list2, *, comp=lambda x, y: x < y):
    """将两个有序列表合并 合并之后仍然有序"""
    list3 = []
    index1, index2 = 0, 0
    while index1 < len(list1) and index2 < len(list2):
        if comp(list1[index1], list2[index2]):
            list3.append(list1[index1])
            index1 += 1
        else:
            list3.append(list2[index2])
            index2 += 1
    list3 += list1[index1:]
    list3 += list2[index2:]
    return list3


# 9, 2, 3, 4, 5, 6, 7, 8, 1
# 函数的参数:
# 1. 位置参数
# 2. 可变参数
# 3. 关键字参数
# 4. 命名关键字参数
def bubble_sort(unsorted_items, *, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = unsorted_items[:]
    items_len = len(items)
    for i in range(items_len - 1):
        swapped = False
        for j in range(items_len - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(items_len - 2 - i, 0, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


# class Student():
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'{self.name}: {self.age}'
#
#     def __gt__(self, other):
#         return self.age > other.age
Student = namedtuple('Student', ('name', 'age'))


def main():
    """主函数"""
    items = [
        Student('Luo Hao', 38), Student('Wang Dachui', 19),
        Student('Lee Xiaolong', 25), Student('Zhang Sanfeng', 120)
    ]
    print(bubble_sort(unsorted_items=items,
                      comp=lambda x, y: x.age > y.age))
    items2 = ['pitaya', 'pear', 'apple', 'watermelon', 'waxberry']
    print(bubble_sort(items2, comp=lambda x, y: len(x) > len(y)))
    items3 = [68, 34, 12, 95, 73, 80, 57]
    print(merge_sort(items3))


if __name__ == '__main__':
    main()
