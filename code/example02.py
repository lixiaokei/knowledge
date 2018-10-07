"""
查找算法

如果列表无序 - 顺序查找
如果列表有序 - 折半查找
"""


def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


def compare(x, y):
    if x == y:
        return 0
    return -1 if x < y else 1


def bin_search(items, key, comp=compare):
    """折半查找(二分查找)"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        result = comp(key, items[mid])
        if result > 0:
            start = mid + 1
        elif result < 0:
            end = mid - 1
        else:
            return mid
    return -1
