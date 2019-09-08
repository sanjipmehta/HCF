def gen():
	x = 0
	while True:
		yield x
		x += 1
y = gen()
print(next(y), end='')
print(next(y), end='')
print(next(y), end='')