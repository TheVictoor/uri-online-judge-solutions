ct = int(input())

for i in range(ct):
	l1 = 0
	#configuração do dado
	#	 A
	#x0-x1-x2-x3
	#	 B
	a = input()
	x = input()
	x = x.split(' ')
	b = input()

	if a == '*' and b == '*':
		l1 += 2
	if x[0] == '*' and x[2] == '*':
		l1 += 2
	if x[1] == '*' and x[3] == '*':
		l1 += 2

	if l1 == 6:
		print(6 * 4 * 2 )
	elif l1 == 4:
		print(4 * 2 )
	elif l1 == 2:
		print(2 * 1)
	else:
		print(1)