t = int(input())
v = []

i = 0
while len(v) < 1001:
	for x in range(t):
		v += [x]
		
for a in range(1000):
	print('N[%d] = %d' %(a , v[a]))