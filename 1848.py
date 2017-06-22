c = 0
while 1:
	try:
		x = input()
		x = x.split(' ')

		if x[0] == '*--':
			c += 4
		elif x[0] == '-*-':
			c += 2
		elif x[0] == '--*':
			c += 1
		elif x[0] == '**-':
			c += 6
		elif x[0] == '*-*':
			c += 5
		elif x[0] == '-**':
			c += 3
		elif x[0] == '***':
			c += 7
		elif x[0] == 'caw':
			print(c)
			c = 0
	except:
		break