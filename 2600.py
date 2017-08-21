n = int(input())

for i in range(n):
	r = 0
	a = int(input())
	b = input()
	b = b.split(' ')
	c = int(input())

	if (a + c) == 7 and (int(b[0]) + int(b[2])) == 7 and (int(b[1]) + int(b[3])) == 7:
		r = 1

	b.append(a)
	b.append(c)
	for i in range(1,len(b)):
		for i in range(1, len(b)):
			if int(b[i-1]) > int(b[i]):
				b[i-1],b[i] = b[i], b[i-1] 

	for i in range(1,7):
		if i != int(b[i-1]):
			r = 0
			break


	if r == 1:
		print('SIM')
	else:
		print('NAO')

