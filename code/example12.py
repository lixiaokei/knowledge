"""
并发编程

多进程 - 计算密集型任务 - 发挥多核特性
多线程 - 非计算密集型任务 - 改善用户体验/占用更多的CPU时间
单线程+异步I/O(多路I/O复用) - I/O密集型任务 - node.js / redis

同步 - 阻塞/等待
异步 - 非阻塞 
"""

def is_valid_for_triangle(a, b, c):
	assert a > 0 and b > 0 and c > 0
	return a + b > c and a + c > b and b + c > a