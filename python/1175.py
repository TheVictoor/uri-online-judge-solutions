v = []

for i in range(20):
	v += [int(input())]

aa = 19
for x in range(10):
	v[x], v[aa] = v[aa], v[x]
	aa -= 1
	

for z in range(20):
	print('N[%d] = %d' %(z , v[z]))