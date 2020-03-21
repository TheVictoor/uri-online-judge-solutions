x = int(input())

v = [x]

for i in range(9):
	x *= 2
	v += [x]

for a in range(10):
	print('N[%d] = %d'%(a , v[a]))