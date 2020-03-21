ct = int(input())

for i in range(ct):
	a = input()
	a = a.split(' ')
	
	b = input()
	b = b.split(' ')

	c = int(b[0]) + int(b[1])

	if c % 2 == 0:
		if a[1] == 'PAR':
			print(a[0])
		else:
			print(a[2])
	else:
		if a[1] == 'IMPAR':
			print(a[0])
		else:
			print(a[2])
