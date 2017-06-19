while 1: 
	x = int(input())

	if x == 0:
		break

	s = 0
	for i in range(10):
		if x % 2 == 0:
			s += x
		x += 1

	print(s)


