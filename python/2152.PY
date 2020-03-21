c = int(input())

for i in range(c):
	x = input()
	x = x.split(' ')

	print('%02d:%02d - ' %(int(x[0]), int(x[1])), end='')

	if x[2] == '1':
		print('A porta abriu!')
	elif x[2] == '0':
		print('A porta fechou!')
