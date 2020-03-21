n = 0

while 1:
	qn = 0

	x = int(input())
	if x == 0:
		break

	for i in range(x):
		c = input()
		c = c.split(' ')

		if c[1] == 'suco':
			n = int(c[0]) * 120
		elif c[1] == 'morango' or c[1] == 'mamao': 
			n = int(c[0]) * 85
		elif c[1] == 'goiaba': 
			n =  int(c[0]) * 70
		elif c[1] == 'manga': 
			n =  int(c[0]) * 56
		elif c[1] == 'laranja': 
			n =  int(c[0]) * 50
		elif c[1] == 'brocolis': 
			n =  int(c[0]) * 34

		qn += n

	if qn > 130:
		print('Menos %d mg' %(qn - 130))
	elif qn < 110:
		print('Mais %d mg' %(110 - qn))
	else:
		print('%d mg' %qn)