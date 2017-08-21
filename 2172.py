while 1:
	x = input()
	x = x.split(' ')

	if x[0] == '0' and x[1] == '0':
		break
	else:
		print(int(x[0]) * int(x[1]))
