while 1:
	q = input()
	q = q.split(' ')

	n = int(q[0])
	x = int(q[1]) 

	if n == x:		
		break

	if n < x:
		print('Crescente')
	else:
		print('Decrescente')
