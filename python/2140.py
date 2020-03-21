#aray com todas as possibilidades de notas 
cc = [4, 7, 10, 12, 15, 20, 22, 25, 30, 40, 52, 55, 60, 70, 100, 102, 105, 110, 120, 150, 200]

while 1:
	x = input()
	x = x.split(' ')
	v = False
	if int(x[0]) == 0 and int(x[1]) == 0:
		break
	else:
		b = int(x[1]) - int(x[0])

		for i in range(len(cc)):
			if b == cc[i]:
				v = True
				break

		if v == True:
			print('possible')
		else:
			print('impossible')