"""
混入(Mixin)
"""


class SetOnce():
	__slots__ = ()
	
	def __setitem__(self, key, value):
		if key in self:
			raise KeyError('不允许为已有的键重新赋值')
		return super().__setitem__(key, value)


class MyDict(SetOnce, dict):
	pass


def main():
	items = MyDict()
	try:
		items['username'] = 'luohao'
		items['username'] = 'wangdachui'
	except KeyError:
		pass
	print(items)


if __name__ == '__main__':
	main()
