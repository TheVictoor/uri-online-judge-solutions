v = []

for i in range(100):
	v += [float(input())]

for a in range(100):
	if v[a] <= 10.0:
		print('A[%d] = %.1f' %(a , v[a]))