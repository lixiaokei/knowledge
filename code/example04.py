"""
生成式(推导式) / 生成器 / 迭代器
"""


def main():
    # scores = [[None] * 3] * 5
    scores = [[None] * 3 for _ in range(5)]
    scores[0][0] = 95
    scores[1][0] = 60
    scores[1][1] = 100
    print(scores)
    prices = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }
    # 用股票价格大于100元的股票构造一个新的字典
    prices_gt100 = {key: value for key, value in prices.items()
                    if value > 100}
    print(prices_gt100)
    # 用4个字符构成的股票代码创建一个集合
    prices_code4 = {key for key in prices if len(key) == 4}
    print(prices_code4)
    # 给字典中的元素按照value的大小排序
    print(dict(sorted(zip(prices.values(), prices.keys()))))
    print(dict(zip('ABCDE', '123456789')))
    # 用生成式(推导式)取代filter和map函数
    items = [13, 25, 44, 12, 98, 67, 30, 33]
    # filter ---> map ---> reduce
    new_items = list(map(lambda x: x ** 2,
                         filter(lambda x: x % 2, items)))
    print(new_items)
    new_items2 = [x ** 2 for x in items if x % 2]
    print(new_items2)


if __name__ == '__main__':
    main()
