x = int(input())

for i in range(x):
	q = input()
	q = q.split(' ')

	a = int(q[0])
	b = int(q[1])

	s = 0
	while 1:
		if b == 0:
			break
		if a % 2 == 1:
			s += a
			b -= 1
		a += 1

	print(s)
