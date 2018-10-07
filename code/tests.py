"""
单元测试 - 针对程序中最小的功能模块(函数/方法)所编写的测试代码
白盒测试(知道代码内部结构)和黑盒测试(对代码内部结构一无所知)
黑盒测试方法 - 给函数传入指定的参数观察实际的输出和预期的输出是否一致

集成测试 ---> 系统测试 ---> 验收测试
Selenium / Robot Framework ---> 自动化测试框架
unittest / django / coverage / mock / tox / pytest

Python中有一个unittest模块对单元测试提供了支持
python3 -m unittest tests.py
"""
from unittest import TestCase

from example02 import seq_search, bin_search


class TestExample02(TestCase):

    def test_seq_search(self):
        items = [68, 34, 12, 95, 73, 80, 57]
        self.assertEqual(0, seq_search(items, 68))
        self.assertEqual(2, seq_search(items, 12))
        self.assertEqual(5, seq_search(items, 80))
        self.assertEqual(6, seq_search(items, 57))
        self.assertEqual(-1, seq_search(items, 66))
        self.assertEqual(-1, seq_search(items, 15))

    def test_bin_search(self):
        items = [12, 24, 35, 52, 67, 79, 80, 81, 93]
        self.assertEqual(0, bin_search(items, 12))
        self.assertEqual(2, bin_search(items, 35))
        self.assertEqual(5, bin_search(items, 79))
        self.assertEqual(7, bin_search(items, 81))
        self.assertEqual(8, bin_search(items, 93))
        self.assertEqual(-1, bin_search(items, 10))
        self.assertEqual(-1, bin_search(items, 100))
