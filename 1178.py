v = [float(input())]

for i in range(1, 100):
	v += [v[i - 1] / 2]

for x in range(100):
	print('N[%d] = %.4f' %(x , v[x]))
